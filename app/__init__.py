import os
import logging
from app.agent import root_agent

os.environ["OTEL_SDK_DISABLED"] = "true"
logging.getLogger("opentelemetry").setLevel(logging.ERROR)

__all__ = ["root_agent"]
