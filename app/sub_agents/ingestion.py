from google.adk import Agent

from app.models import claude
from app.prompts import ingestion

ingestion_agent = Agent(
    model=claude,
    name="ingestion_agent",
    instruction=ingestion.prompt,
    description="You are an llm agent",
)
