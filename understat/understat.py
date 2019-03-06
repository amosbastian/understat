import asyncio
import re

import aiohttp
from bs4 import BeautifulSoup

from understat.constants import LEAGUE_URL, PATTERN
from understat.utils import decode_data, fetch, find_match, to_league_name


class Understat():
    def __init__(self, session):
        self.session = session

    async def get_teams(self, league_name, season):
        """Returns a dictionary containing information about all the teams in
        the given league in the given season.

        :param league_name: The league's name.
        :type league_name: str
        :param season: The season.
        :type season: str or int
        :return: A dictionary of the league's table as seen on Understat.
        :rtype: dict
        """

        league_name = to_league_name(league_name)
        url = LEAGUE_URL.format(league_name, season)

        html = await fetch(self.session, url)
        soup = BeautifulSoup(html, "html.parser")
        scripts = soup.find_all("script")

        pattern = re.compile(PATTERN.format("teamsData"))
        match = find_match(scripts, pattern)
        team_data = decode_data(match)

        return team_data
