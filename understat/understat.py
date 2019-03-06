import asyncio
import re

import aiohttp
from bs4 import BeautifulSoup

from understat.constants import LEAGUE_URL
from understat.utils import (decode_data, fetch, find_match, get_data,
                             to_league_name)


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

        url = LEAGUE_URL.format(to_league_name(league_name), season)
        team_data = await get_data(self.session, url, "teamsData")

        return team_data

    async def get_players(self, league_name, season):
        url = LEAGUE_URL.format(to_league_name(league_name), season)
        players_data = await get_data(self.session, url, "playersData")

        return players_data

    async def get_results(self, league_name, season):
        url = LEAGUE_URL.format(to_league_name(league_name), season)
        dates_data = await get_data(self.session, url, "datesData")
        results = [r for r in dates_data if r["isResult"]]

        return results

    async def get_fixtures(self, league_name, season):
        url = LEAGUE_URL.format(to_league_name(league_name), season)
        dates_data = await get_data(self.session, url, "datesData")
        fixtures = [f for f in dates_data if not f["isResult"]]

        return fixtures
