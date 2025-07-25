import os

import django
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

# setup django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dojo.settings.settings")
django.setup()

from dojo.filters import ApiFindingFilter  # noqa: E402
from dojo.models import Finding  # noqa: E402

app = FastAPI(title="DefectDojo MCP")


class InitResponse(BaseModel):
    name: str
    description: str
    version: str
    endpoints: list[str]

class FindingOut(BaseModel):
    id: int
    title: str
    severity: str
    url: str | None


class SLAOut(BaseModel):
    id: int
    title: str
    sla_expiration_date: str | None


@app.get("/")
def root():
    """Health check endpoint for Copilot."""
    return {"status": "ok"}


@app.post("/initialize", response_model=InitResponse)
def initialize():
    """Return basic metadata so Copilot can connect."""
    return InitResponse(
        name="DefectDojo MCP",
        description="Query findings from DefectDojo",
        version="1.0",
        endpoints=[
            "/findings",
            "/findings/{severity}",
            "/risk-accepted",
            "/critical-sla",
        ],
    )

@app.get("/findings", response_model=list[FindingOut])
def list_findings(request: Request):
    params = dict(request.query_params)
    f = ApiFindingFilter(params, queryset=Finding.objects.all())
    if not f.is_valid():
        raise HTTPException(status_code=400, detail=f.errors)
    return [
        FindingOut(id=fi.id, title=fi.title, severity=fi.severity, url=fi.file_path)
        for fi in f.qs
    ]


@app.get("/findings/{severity}", response_model=list[FindingOut])
def findings_by_severity(severity: str, request: Request):
    params = dict(request.query_params)
    params["severity"] = severity
    f = ApiFindingFilter(params, queryset=Finding.objects.all())
    if not f.is_valid():
        raise HTTPException(status_code=400, detail=f.errors)
    return [
        FindingOut(id=fi.id, title=fi.title, severity=fi.severity, url=fi.file_path)
        for fi in f.qs
    ]


@app.get("/risk-accepted", response_model=list[FindingOut])
def list_risk_accepted():
    qs = Finding.objects.filter(risk_accepted=True)
    return [FindingOut(id=f.id, title=f.title, severity=f.severity, url=f.file_path) for f in qs]


@app.get("/critical-sla", response_model=list[SLAOut])
def critical_sla():
    qs = Finding.objects.filter(severity="Critical")
    return [
        SLAOut(
            id=f.id,
            title=f.title,
            sla_expiration_date=f.sla_expiration_date.isoformat()
            if f.sla_expiration_date
            else None,
        )
        for f in qs
    ]

