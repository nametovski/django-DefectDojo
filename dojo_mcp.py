from __future__ import annotations

import logging
import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

API_URL = os.environ.get("DEFECTDOJO_API_URL", "http://localhost:8080/api/v2")
API_TOKEN = os.environ.get("DEFECTDOJO_API_TOKEN")

# Configure FastMCP server to listen on all interfaces by default
mcp = FastMCP(
    "dojo",
    host=os.environ.get("FASTMCP_HOST", "0.0.0.0"),  # noqa: S104
    port=int(os.environ.get("FASTMCP_PORT", "8010")),
)

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
_log.info("Starting Dojo MCP server, API_URL=%s", API_URL)

_session = httpx.Client(headers={"Authorization": f"Token {API_TOKEN}"} if API_TOKEN else {}, timeout=30)


def _api_get(path: str, params: dict[str, Any] | None = None) -> Any:
    """Helper to GET objects from the DefectDojo API."""
    url = f"{API_URL.rstrip('/')}/{path.lstrip('/')}"
    response = _session.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    # many API endpoints are paginated
    return data.get("results", data)


@mcp.tool()
def list_products() -> list[dict]:
    """Return all products."""
    return _api_get("products/")


@mcp.tool()
def list_engagements(product_id: int | None = None) -> list[dict]:
    """Return engagements, optionally filtered by product."""
    params = {"product": product_id} if product_id else None
    return _api_get("engagements/", params)


@mcp.tool()
def list_findings(
    severity: str | None = None,
    product_id: int | None = None,
    engagement_id: int | None = None,
) -> list[dict]:
    """List findings using DefectDojo filters."""
    params: dict[str, Any] = {}
    if severity:
        params["severity"] = severity
    if product_id:
        params["test__engagement__product"] = product_id
    if engagement_id:
        params["test__engagement"] = engagement_id
    return _api_get("findings/", params)


@mcp.tool()
def findings_outside_sla() -> list[dict]:
    """Return findings that violate SLA."""
    return _api_get("findings/", {"outside_of_sla": 1})


@mcp.tool()
def list_risk_accepted() -> list[dict]:
    """Return risk-accepted findings."""
    return _api_get("findings/", {"status": 5})


@mcp.tool()
def critical_sla() -> list[dict]:
    """Return critical findings that violate SLA."""
    return _api_get("findings/", {"severity": "Critical", "outside_of_sla": 1})


@mcp.tool()
def update_finding_status(finding_id: int, **fields: Any) -> dict:
    """Update fields on a finding."""
    url = f"{API_URL.rstrip('/')}/findings/{finding_id}/"
    response = _session.patch(url, json=fields)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def benchmark_results(product_id: int) -> list[dict]:
    """Return benchmark requirements for a product."""
    return _api_get(f"benchmarks/{product_id}/")


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
