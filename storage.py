import os
from utils import get_week_filename, get_today_label, format_entry


def list_markdown_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith(".md")]
    files.sort()
    return files


def read_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def ensure_week_file(directory):
    filename = get_week_filename()
    filepath = os.path.join(directory, filename)

    if not os.path.exists(filepath):
        create_empty_week_file(filepath)

    return filepath


def create_empty_week_file(filepath):
    from datetime import datetime, timedelta

    today = datetime.today()
    monday = today - timedelta(days=today.weekday())

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(
            f"# Reporting vom {monday.strftime('%d. %B')} - {(monday + timedelta(days=4)).strftime('%d. %B %Y')}\n"
        )

        for i in range(5):
            day = monday + timedelta(days=i)
            f.write(f"\n## Reporting {day.strftime('%d. %B')}\n\n")
            f.write("Zeit            | Aktivität     | Doing\n")
            f.write("--------------- | ------------- | ------------------\n")


def add_entry_to_today(filepath, time_from, time_to, activity, doing):
    def parse_start_time(line):
        try:
            time_part = line.split("|")[0].strip()
            start = time_part.split("-")[0].strip()
            h, m = start.split(":")
            return int(h) * 60 + int(m)
        except:
            return 9999

    today_label = get_today_label()
    new_entry = format_entry(time_from, time_to, activity, doing)

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    inside_section = False
    entries = []
    inserted = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # 👉 Start der richtigen Section
        if line.strip() == f"## Reporting {today_label}":
            inside_section = True
            result.append(line)
            i += 1
            continue

        if inside_section:
            result.append(line)

            # Header
            if "Zeit" in line and "Aktivität" in line:
                i += 1
                continue

            # Separator
            if "---" in line:
                i += 1

                # 👉 Bestehende Einträge sammeln (ohne Leerzeilen)
                j = i
                while j < len(lines) and not lines[j].startswith("## Reporting"):
                    if lines[j].strip():
                        entries.append(lines[j])
                    j += 1

                # 👉 neuen Eintrag hinzufügen
                entries.append(new_entry)

                # 👉 sortieren (ASC)
                entries.sort(key=parse_start_time)

                # 👉 sauber einfügen
                for e in entries:
                    result.append(e)

                # 👉 GENAU eine Leerzeile vor nächster Section
                result.append("\n")

                inserted = True
                inside_section = False
                i = j
                continue

        else:
            result.append(line)

        i += 1

    # fallback
    if not inserted:
        result.append(new_entry)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(result)