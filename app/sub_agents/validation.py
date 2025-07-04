from google.adk import Agent

from app.models import claude
from app.prompts import validation
from app.tools.validation import validate_subscriptions_tool

validation_agent = Agent(
    model=claude,
    name="validation_agent",
    instruction=validation.prompt,
    description="You are an llm agent",
    tools=[validate_subscriptions_tool]
)
