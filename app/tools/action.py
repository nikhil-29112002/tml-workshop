import requests
from datetime import datetime, timedelta
from google.adk.tools import FunctionTool

from app.records import invalid_records


def fix_record(record):
    renewal_date = datetime.strptime(record["renewal_date"], "%Y-%m-%d")
    expected_validity_end_date = renewal_date + timedelta(days=365)

    return {
        "id": record[id],
        "iccid": record["iccid"],
        "subscription_status_at_l4": record["subscription_status_at_l4"],
        "validity_end_date": expected_validity_end_date,
    }


def sync_subscription():
    records = invalid_records.get()
    fixed_records = list(map(fix_record, records))

    requests.post(
        "https://skindev-new-pv.api.tatamotors/api/cvp_demo/data/update_renewal_data/",
        json=fixed_records,
    )

    return f"Fixed records {len(fixed_records)}"


sync_subscription_tool = FunctionTool(sync_subscription)
