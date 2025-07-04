from google.adk import Agent

from prompts import ingestion

MODEL = "gemini-2.5-pro"

ingestion_agent = Agent(
    model=MODEL, name="ingestion agent", instruction=ingestion.prompt
)
