from google.adk import Agent

from models import claude
from prompts import notification

notification_agent = Agent(
    model=claude, name="notification_agent", instruction=notification.prompt
)
