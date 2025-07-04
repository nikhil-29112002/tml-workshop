import os
from app.agent import root_agent

os.environ["OTEL_SDK_DISABLED"] = "true"

__all__ = ["root_agent"]
