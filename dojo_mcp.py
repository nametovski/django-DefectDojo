from __future__ import annotations

import logging
import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

API_URL = os.environ.get("DEFECTDOJO_API_URL", "http://localhost:8080/api/v2")
API_TOKEN = os.environ.get("DEFECTDOJO_API_TOKEN")
API_USER = os.environ.get("DEFECTDOJO_API_USER")
API_PASSWORD = os.environ.get("DEFECTDOJO_API_PASSWORD")

# Configure FastMCP server to listen on all interfaces by default
mcp = FastMCP(
    "dojo",
    host=os.environ.get("FASTMCP_HOST", "0.0.0.0"),  # noqa: S104
    port=int(os.environ.get("FASTMCP_PORT", "8010")),
)

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
_log.info("Starting Dojo MCP server, API_URL=%s", API_URL)

_session = httpx.Client(timeout=30)
if API_TOKEN:
    _session.headers["Authorization"] = f"Token {API_TOKEN}"
elif API_USER and API_PASSWORD:
    resp = _session.post(
        f"{API_URL.rstrip('/')}/api-token-auth/",
        json={"username": API_USER, "password": API_PASSWORD},
    )
    if resp.status_code == 200:
        token = resp.json().get("token")
        if token:
            _session.headers["Authorization"] = f"Token {token}"


def _api_get(path: str, params: dict[str, Any] | None = None) -> Any:
    """Helper to GET objects from the DefectDojo API."""
    url = f"{API_URL.rstrip('/')}/{path.lstrip('/')}"
    response = _session.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    # many API endpoints are paginated
    return data.get("results", data)


def _api_post(path: str, payload: dict[str, Any]) -> dict:
    """POST data to the DefectDojo API and return the created object."""
    url = f"{API_URL.rstrip('/')}/{path.lstrip('/')}"
    response = _session.post(url, json=payload)
    response.raise_for_status()
    return response.json()


def _api_patch(path: str, payload: dict[str, Any]) -> dict:
    """PATCH data to the DefectDojo API and return the updated object."""
    url = f"{API_URL.rstrip('/')}/{path.lstrip('/')}"
    response = _session.patch(url, json=payload)
    response.raise_for_status()
    return response.json()


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
    return _api_patch(f"findings/{finding_id}/", fields)


@mcp.tool()
def benchmark_results(product_id: int) -> list[dict]:
    """Return benchmark requirements for a product."""
    return _api_get(f"benchmarks/{product_id}/")


@mcp.tool()
def create_engagement(name: str, product_id: int, **fields: Any) -> dict:
    """Create a new engagement under the given product."""
    payload = {"name": name, "product": product_id}
    payload.update(fields)
    return _api_post("engagements/", payload)


@mcp.tool()
def list_tests(engagement_id: int) -> list[dict]:
    """List tests for an engagement."""
    return _api_get("tests/", {"engagement": engagement_id})


@mcp.tool()
def create_test(engagement_id: int, test_type: int, **fields: Any) -> dict:
    """Create a test in an engagement."""
    payload = {"engagement": engagement_id, "test_type": test_type}
    payload.update(fields)
    return _api_post("tests/", payload)


@mcp.tool()
def create_finding(test_id: int, title: str, severity: str, **fields: Any) -> dict:
    """Create a finding under a test."""
    payload = {"test": test_id, "title": title, "severity": severity}
    payload.update(fields)
    return _api_post("findings/", payload)


def _epss_lookup(cve: str) -> dict | None:
    url = "https://api.first.org/data/v1/epss"
    resp = httpx.get(url, params={"cve": cve}, timeout=30)
    if resp.status_code == 200:
        data = resp.json().get("data")
        return data[0] if data else None
    return None


def _kev_lookup(cve: str) -> dict | None:
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    resp = httpx.get(url, timeout=30)
    if resp.status_code == 200:
        items = resp.json().get("vulnerabilities", [])
        for item in items:
            if item.get("cveID") == cve:
                return item
    return None


@mcp.tool()
def epss_score(cve: str) -> dict | None:
    """Return EPSS data for a CVE."""
    return _epss_lookup(cve)


@mcp.tool()
def kev_entry(cve: str) -> dict | None:
    """Return KEV catalog entry for a CVE if present."""
    return _kev_lookup(cve)


@mcp.tool()
def enrich_finding_epss(finding_id: int) -> dict | None:
    """Get EPSS data for a finding's CVE."""
    finding = _api_get(f"findings/{finding_id}/")
    cve = finding.get("cve")
    return _epss_lookup(cve) if cve else None


@mcp.tool()
def enrich_finding_kev(finding_id: int) -> dict | None:
    """Get KEV entry for a finding's CVE."""
    finding = _api_get(f"findings/{finding_id}/")
    cve = finding.get("cve")
    return _kev_lookup(cve) if cve else None


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
