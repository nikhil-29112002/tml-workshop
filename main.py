from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from prompts import master
from sub_agents import ingestion, validation, notification

MODEL = "gemini-2.5-pro"


service_agent = LlmAgent(
    name="master agent for corrdinating",
    model=MODEL,
    instruction=master.prompt,
    output_key="response",
    tools=[
        AgentTool(agent=ingestion.ingestion_agent),
        AgentTool(agent=validation.validation_agent),
        AgentTool(agent=notification.notification_agent),
    ],
)

root_agent = service_agent
