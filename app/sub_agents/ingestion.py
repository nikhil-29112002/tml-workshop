from google.adk import Agent

from app.models import claude
from app.prompts import ingestion
from app.tools.ingestion import get_renewed_subscriptions_tool


ingestion_agent = Agent(
    model=claude,
    name="ingestion_agent",
    instruction=ingestion.prompt,
    description="You are an llm agent",
    tools=[get_renewed_subscriptions_tool],
)
