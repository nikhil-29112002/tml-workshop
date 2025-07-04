from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from app.models import claude
from app.prompts import master
from app.sub_agents import ingestion, validation, notification


service_agent = LlmAgent(
    name="master_agent",
    model=claude,
    description="You are an llm agent",
    instruction=master.prompt,
    output_key="response",
    tools=[
        AgentTool(agent=ingestion.ingestion_agent),
        AgentTool(agent=validation.validation_agent),
        AgentTool(agent=notification.notification_agent),
    ],
)

root_agent = service_agent
