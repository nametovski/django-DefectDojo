from __future__ import annotations

import logging
import os

import httpx
from mcp.server.fastmcp import FastMCP

FASTAPI_URL = os.environ.get("FASTAPI_URL", "http://127.0.0.1:8000")

# Configure FastMCP server. Use env vars FASTMCP_HOST/FASTMCP_PORT if set.
mcp = FastMCP(
    "dojo",
    host=os.environ.get("FASTMCP_HOST", "127.0.0.1"),
    port=int(os.environ.get("FASTMCP_PORT", "8010")),
)

logging.basicConfig(level=logging.INFO)
logging.getLogger(__name__).info("Starting Dojo MCP server, FASTAPI_URL = %s", FASTAPI_URL)


@mcp.tool()
def list_findings(severity: str | None = None) -> list[dict]:
    """List findings optionally filtered by severity."""
    params = {}
    if severity:
        params["severity"] = severity
    response = httpx.get(f"{FASTAPI_URL}/findings", params=params, timeout=30)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def list_risk_accepted() -> list[dict]:
    """List risk-accepted findings."""
    response = httpx.get(f"{FASTAPI_URL}/risk-accepted", timeout=30)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def critical_sla() -> list[dict]:
    """List SLA info for critical findings."""
    response = httpx.get(f"{FASTAPI_URL}/critical-sla", timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
