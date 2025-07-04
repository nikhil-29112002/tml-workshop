from google.adk.agents import LlmAgent

from app.models import claude
from app.prompts import master
from app.sub_agents import ingestion, validation, notification, action


service_agent = LlmAgent(
    name="master_agent",
    model=claude,
    description="You are an llm agent",
    instruction=master.prompt,
    output_key="response",
    sub_agents=[
        ingestion.ingestion_agent,
        validation.validation_agent,
        notification.notification_agent,
        action.action_agent,
    ],
)

root_agent = service_agent
