import os

from google.adk.models.lite_llm import LiteLlm

import dotenv

llm_model = os.getenv("LLM_MODEL")
assert llm_model is not None

dotenv.load_dotenv(llm_model)

claude = LiteLlm(
    "bedrock/arn:aws:bedrock:eu-west-1:604233880530:inference-profile/eu.anthropic.claude-3-5-sonnet-20240620-v1:0"
)
