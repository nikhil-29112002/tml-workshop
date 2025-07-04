from google.adk import Agent

from app.models import claude
from app.prompts import validation

validation_agent = Agent(
    model=claude, name="validation_agent", instruction=validation.prompt
)
