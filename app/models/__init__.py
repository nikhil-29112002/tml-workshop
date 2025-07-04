from google.adk.models.lite_llm import LiteLlm

import dotenv

dotenv.load_dotenv()

claude = LiteLlm("anthropic.claude-3-5-sonnet-20240620-v1:0")
