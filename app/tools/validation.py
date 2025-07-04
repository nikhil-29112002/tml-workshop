from datetime import datetime, timedelta
from google.adk.tools import FunctionTool
from app.records import records, invalid_records


def _validate_record(record) -> bool:
    if record["renewal_date"] is None or record["validity_end_date"] is None:
        return False

    renewal_date = datetime.strptime(record["renewal_date"], "%Y-%m-%d")
    expected_validity_end_date = renewal_date + timedelta(days=365)

    actual_validity_end_date = datetime.strptime(
        record["validity_end_date"], "%Y-%m-%d"
    )
    return expected_validity_end_date != actual_validity_end_date


async def validate_subscriptions():
    """
    This tool validates renewed subscriptions
    """
    data = records.get()
    filtered_data = list(filter(_validate_record, data["data"]))
    invalid_records.set(filtered_data)

    return f"Number of invalid records {len(filtered_data)}"


validate_subscriptions_tool = FunctionTool(validate_subscriptions)
