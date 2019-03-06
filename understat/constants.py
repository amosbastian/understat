import re

LEAGUE_URL = "https://understat.com/league/{}"
PLAYERS_PATTERN = "var\s+playersData\s+=\s+JSON.parse\(\'(.*?)\'\);"
