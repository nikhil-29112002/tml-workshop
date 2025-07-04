from google.adk import Agent

from models import claude
from prompts import ingestion

ingestion_agent = Agent(
    model=claude, name="ingestion_agent", instruction=ingestion.prompt
)
