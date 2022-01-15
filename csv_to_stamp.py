import csv
import sys
import re
from pyperclip import copy


def seconds_to_timestamp(total_seconds: int) -> str:
    hours = total_seconds // 3600
    minutes = (total_seconds - hours*3600) // 60
    seconds = total_seconds - hours*3600 - minutes*60
    return f"{hours:01d}:{minutes:02d}:{seconds:02d}"


def url_to_timestamp(url: str) -> str:
    seconds_match = re.search(r't=([0-9]+)', url)
    if seconds_match:
        return seconds_to_timestamp(int(seconds_match.group(1)))
    else:
        return seconds_to_timestamp(0) 


if __name__ == '__main__':
    output = ""
    output += "Bracket: \n"
    with open(sys.argv[1]) as csvfile: 
        reader = csv.DictReader(csvfile)
        for row in reader:
            output += f"{url_to_timestamp(row['URL'])} {row['P1Name']} vs {row['P2Name']}\n"
    output += "\nTwitch: https://www.twitch.tv/skullgirlsoceania\n" \
          "Twitter: https://twitter.com/SkullgirlsOCE\n" \
          "Discord: https://discord.gg/WKG373f\n" \
          "VOD archive: https://slowtrainroll.in/" 
    print(output)
    copy(output)
    input("\nPress Enter to continue...")