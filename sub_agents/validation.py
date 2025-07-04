from google.adk import Agent

from models import claude
from prompts import validation

validation_agent = Agent(
    model=claude, name="validation_agent", instruction=validation.prompt
)
