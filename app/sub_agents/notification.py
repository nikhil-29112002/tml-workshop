from google.adk import Agent

from app.models import claude
from app.prompts import notification
from app.tools.notification import send_notification_tool

notification_agent = Agent(
    model=claude,
    name="notification_agent",
    instruction=notification.prompt,
    description="You are an llm agent",
    tools=[send_notification_tool]
)
