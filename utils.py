from datetime import datetime, timezone, timedelta


def get_adjusted_time(timezone_offset: str) -> str:
    try:
        hours, minutes = map(int, timezone_offset.split(":"))
        offset = timedelta(hours=hours, minutes=minutes)
    except ValueError:
        raise ValueError("Invalid timezone format. Use ±HH:MM format.")

    current_time = datetime.now(timezone.utc)

    adjusted_time = current_time + offset

    return adjusted_time.isoformat()
