import os
import django
from django.db.models import Q
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel

# setup django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dojo.settings.settings')
django.setup()

from dojo.models import Finding  # noqa: E402
from dojo.filters import ApiFindingFilter  # noqa: E402

app = FastAPI(title="DefectDojo MCP")

class FindingOut(BaseModel):
    id: int
    title: str
    severity: str
    url: str | None

class SLAOut(BaseModel):
    id: int
    title: str
    sla_expiration_date: str | None


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
    items = []
    for f in qs:
        items.append(SLAOut(id=f.id, title=f.title, sla_expiration_date=f.sla_expiration_date.isoformat() if f.sla_expiration_date else None))
    return items

