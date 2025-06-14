import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from google.adk.agents import Agent


def get_current_time(timezone_str: str) -> dict:
    """Returns the current time in a specified IANA timezone.

    Args:
        timezone_str: The IANA timezone name (e.g., 'Asia/Taipei', 'America/New_York').

    Returns:
        dict: A dictionary with the status and the result or an error message.
    """
    try:
        tz = ZoneInfo(timezone_str)

        current_time = datetime.datetime.now(tz)

        time_report = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        report = f"The current time in {timezone_str} is {time_report}."

        return {"status": "success", "report": report}
    except ZoneInfoNotFoundError:
        error_msg = f"Error: Timezone '{timezone_str}' not found. Please use a valid IANA timezone name."

        return {"status": "error", "report": error_msg}
    except Exception as e:
        error_msg = f"An unexpected error occurred: {e}"
        return {"status": "error", "report": error_msg}


root_agent = Agent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
)
