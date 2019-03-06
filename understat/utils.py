import codecs
import json
import re


def to_league_name(league_name):
    league_mapper = {
        "epl": "EPL",
        "la_liga": "La_liga",
        "bundesliga": "Bundesliga",
        "serie_a": "Serie_A",
        "ligue_1": "Ligue_1",
        "rfpl": "RFPL"
    }
    return league_mapper[league_name]


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


def find_match(scripts, pattern):
    for script in scripts:
        match = re.search(pattern, script.string)
        if match:
            break

    return match


def decode_data(match):
    byte_data = codecs.escape_decode(match.group(1))
    json_data = json.loads(byte_data[0].decode("utf-8"))

    return json_data
