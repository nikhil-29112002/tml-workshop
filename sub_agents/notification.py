from google.adk import Agent

from prompts import notification

MODEL = "gemini-2.5-pro"

notification_agent = Agent(
    model=MODEL, name="notification agent", instruction=notification.prompt
)
