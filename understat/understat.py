import asyncio
import codecs
import json

import aiohttp
from bs4 import BeautifulSoup

from understat.constants import LEAGUE_URL


class Understat():
    def __init__(self, session):
        self.session = session

    async def get_league(league_name):
