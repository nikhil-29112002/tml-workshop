from google.adk import Agent

from app.models import claude
from app.prompts import ingestion
from app.tools.ingestion import get_subscription_renewal

ingestion_agent = Agent(
    model=claude,
    name="ingestion_agent",
    instruction=ingestion.prompt,
    description="You are an llm agent",
    tools=[get_subscription_renewal],
)
