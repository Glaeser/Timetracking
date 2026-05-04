from datetime import datetime, timedelta
import locale

# deutsche Monatsnamen erzwingen
try:
    locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
except:
    try:
        locale.setlocale(locale.LC_TIME, "de_DE")
    except:
        pass


def get_current_week_range():
    today = datetime.today()
    monday = today - timedelta(days=today.weekday())
    friday = monday + timedelta(days=4)
    return monday, friday


def get_week_filename():
    monday, friday = get_current_week_range()
    return f"{monday.strftime('%Y-%m-%d')} bis {friday.strftime('%Y-%m-%d')}.md"


def get_today_label():
    today = datetime.today()
    return today.strftime("%d. %B")


def normalize_time(value: str) -> str:
    value = value.strip()

    # Punkt → Doppelpunkt
    value = value.replace(".", ":")

    if ":" in value:
        parts = value.split(":")
        hour = int(parts[0])
        minute = int(parts[1])
    else:
        hour = int(value)
        minute = 0

    if hour > 23 or minute > 59:
        raise ValueError("Ungültige Zeit")

    return f"{hour:02d}:{minute:02d}"


def format_entry(time_from, time_to, activity, doing):
    time_col = f"{time_from} - {time_to}".ljust(15)
    activity_col = f"{activity or ''}".ljust(13)
    doing_col = f"{doing}"

    return f"{time_col} | {activity_col} | {doing_col}\n"