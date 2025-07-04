from google.adk.tools import FunctionTool


def send_notification():
    """
    This tool sends notification
    """

    return "Sent email"


send_notification_tool = FunctionTool(send_notification)
