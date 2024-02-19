from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel
from typing import Union
app = FastAPI()

class SpaceProbe(BaseModel):
    identifier: str
    mission: Union[str, None] = None
    velocity: float
    fuel_level: Union[float, None] = None

@app.post('/space-probe/')
async def register_probe(probe: SpaceProbe):
    # return probe
    probe_report = probe.dict()
    if probe.fuel_level:
        fuel_status = "Sufficient" if probe.fuel_level > 20 else 'Low'
        probe_report.update({"fuel-status": fuel_status})

    return probe_report

@app.put('/space-probe/probe_id')
async def update_probe(probe_id: int, probe: SpaceProbe, q: Union[str, None] = None):
    response = {"probe_id": probe_id, **probe.dict()}
    if q:
        response.update({"additional_query":q})

    return response

