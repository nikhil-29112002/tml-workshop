from google.adk.tools import FunctionTool
import requests
from app.records import records


async def get_renewed_subscriptions():
    """
    This tool returns all renwed subscriptions

    """
    response = requests.get(
        "https://skindev-new-pv.api.tatamotors/api/cvp_demo/data/update_renewal_data/"
    )
    data = response.json()
    records["data"] = data

    return f"received records {len(data)}"


get_renewed_subscriptions_tool = FunctionTool(get_renewed_subscriptions)
