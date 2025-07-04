from google.adk import Agent

from app.models import claude
from app.prompts import action
from app.tools.action import sync_subscription_tool

action_agent = Agent(
    model=claude,
    name="action_agent",
    instruction=action.prompt,
    description="You are an llm agent",
    tools=[sync_subscription_tool],
)
