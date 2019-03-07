import aiohttp
import pytest

from understat import Understat
from understat.utils import (filter_by_positions, filter_data, find_match,
                             to_league_name)


class TestUtils(object):
    @staticmethod
    def test_to_league_name():
        leagues = ["epl", "la_liga", "bundesliga", "serie_a", "ligue_1", "rfpl"]
        leagues = [to_league_name(league) for league in leagues]
        assert leagues == [
            "EPL", "La_liga", "Bundesliga", "Serie_A", "Ligue_1", "RFPL"]

    @staticmethod
    def test_filter_data():
        leagues = [
            {"league": "epl", "players": 600},
            {"league": "la_liga", "players": 300},
            {"league": "bundesliga", "players": 400},
            {"league": "serie_a", "players": 500},
            {"league": "ligue_1", "players": 600},
            {"league": "rfpl", "players": 700}
        ]
        filtered_leagues = filter_data(leagues, {"league": "epl"})
        assert filtered_leagues == [{"league": "epl", "players": 600}]

        filtered_leagues = filter_data(leagues, {"players": 600})
        assert filtered_leagues == [
            {"league": "epl", "players": 600},
            {"league": "ligue_1", "players": 600}
        ]

    @staticmethod
    def test_filter_by_positions():
        data = {"FW": {"goals": {"avg": 0.0042}},
                "Sub": {"goals": {"avg": 0.0026}}}
        filtered_data = filter_by_positions(data, None)
        assert filtered_data == [{"goals": {"avg": 0.0042}, "position": "FW"},
                                 {"goals": {"avg": 0.0026}, "position": "Sub"}]

        filtered_data = filter_by_positions(data, "FW")
        assert filtered_data == [{"goals": {"avg": 0.0042}, "position": "FW"}]
