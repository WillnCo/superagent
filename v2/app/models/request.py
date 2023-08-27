from pydantic import BaseModel
from typing import Optional, Dict


class Agent(BaseModel):
    isActive: bool = True
    name: str


class AgentLLM(BaseModel):
    llmId: str


class AgentDatasource(BaseModel):
    datasourceId: str


class Datasource(BaseModel):
    name: str
    description: str
    type: str
    url: Optional[str]


class LLM(BaseModel):
    provider: str
    model: str
    apiKey: str
    options: Optional[Dict]