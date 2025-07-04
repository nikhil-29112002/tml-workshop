from google.adk import Agent

from prompts import validation

MODEL = "gemini-2.5-pro"

validation_agent = Agent(
    model=MODEL, name="validation agent", instruction=validation.prompt
)
