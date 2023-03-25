import csv
import sys
import re
from pyperclip import copy


def total_seconds_to_timestamp(total_seconds: int) -> str:
    hours = total_seconds // 3600
    minutes = (total_seconds - hours*3600) // 60
    seconds = total_seconds - hours*3600 - minutes*60
    return f"{hours:01d}:{minutes:02d}:{seconds:02d}"


def hms_to_timestamp(h: int, m: int, s: int) -> str:
    return f"{h:01d}:{m:02d}:{s:02d}"


def format_team(c1: str, c2: str, c3: str) -> str:
    ret = c1
    if c2 != "N":
        ret += f"/{c2}"
    if c3 != "N":
        ret += f"/{c3}"
    return ret


def url_to_timestamp(url: str) -> str:
    timestamp_match = re.search(r'[?&]t=([0-9hms]+)', url)

    # If there is no timestamp then it's probably just the start of the video
    if not timestamp_match: 
        return "0:00:00"

    timestamp = timestamp_match.group(1)

    # If this is a simple timestamp with total seconds eg. t=12345, do that
    total_seconds_match = re.fullmatch(r'([0-9]+)', timestamp)
    if total_seconds_match:
        return total_seconds_to_timestamp(int(total_seconds_match.group(1)))

    # If the timestamp has h/m/s fields, extract them
    h_match = re.search(r'([0-9]+)h', timestamp)
    s_match = re.search(r'([0-9]+)s', timestamp)
    m_match = re.search(r'([0-9]+)m', timestamp)
    if h_match:
        h = int(h_match.group(1))
    else:
        h = 0
    if m_match:
        m = int(m_match.group(1))
    else:
        m = 0
    if s_match:
        s = int(s_match.group(1))
    else:
        s = 0
    return hms_to_timestamp(h, m, s)


if __name__ == '__main__':
    output = ""
    output += "Timestamps: \n"
    with open(sys.argv[1]) as csvfile: 
        reader = csv.DictReader(csvfile)
        for row in reader:
            output += f"{url_to_timestamp(row['URL'])} {row['P1Name']} ({format_team(row['P1Char1'],row['P1Char2'],row['P1Char3'])}) vs {row['P2Name']} ({format_team(row['P2Char1'],row['P2Char2'],row['P2Char3'])}) \n"

    output += "\nTimestamps without teams: \n"
    with open(sys.argv[1]) as csvfile: 
        reader = csv.DictReader(csvfile)
        for row in reader:
            output += f"{url_to_timestamp(row['URL'])} {row['P1Name']} vs {row['P2Name']}\n"

    print(output)
    copy(output)
    input("\nPress Enter to continue...")