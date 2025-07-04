from google.adk.tools import FunctionTool
import requests
from app.records import records


async def get_renewed_subscriptions():
    """
    This tool returns all renwed subscriptions

    """
    response = requests.get(
        "https://skindev-new-pv.api.tatamotors/api/cvp_demo/get/cvp_demo/data/renewal/"
    )
    data = response.json()
    records.set(data)

    return f"received records {len(data)}"


get_subscription_renewal = FunctionTool(get_renewed_subscriptions)
