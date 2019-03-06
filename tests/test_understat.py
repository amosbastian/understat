import aiohttp
import pytest

from understat import Understat


leagues = ["epl", "la_liga", "bundesliga", "serie_a", "ligue_1", "rfpl"]


class TestUnderstat(object):
    async def test_init(self, loop):
        session = aiohttp.ClientSession()
        understat = Understat(session)
        assert understat.session is session
        await session.close()

    async def test_get_teams(self, loop, understat):
        for league in leagues:
            teams = await understat.get_teams(league, 2018)
            assert isinstance(teams, list)

    async def test_get_team_with_options(self, loop, understat):
        team = await understat.get_teams(
            "epl", 2018, {"title": "Manchester United"})
        assert isinstance(team, list)
        assert len(team) == 1

        team = await understat.get_teams(
            "epl", 2018, title="Manchester United")
        assert isinstance(team, list)
        assert len(team) == 1

        team = await understat.get_teams("epl", 2018, title="Reddit United")
        assert isinstance(team, list)
        assert not team

    async def test_get_players(self, loop, understat):
        for league in leagues:
            players = await understat.get_players(league, 2018)
            assert isinstance(players, list)

    async def test_get_results(self, loop, understat):
        for league in leagues:
            results = await understat.get_results(league, 2018)
            assert isinstance(results, list)

        for result in results:
            assert result["isResult"]

    async def test_get_fixtures(self, loop, understat):
        for league in leagues:
            fixtures = await understat.get_fixtures(league, 2018)
            assert isinstance(fixtures, list)

        for fixture in fixtures:
            assert not fixture["isResult"]

    async def test_get_player_shots(self, loop, understat):
        player_shots = await understat.get_player_shots(619)
        assert isinstance(player_shots, list)

        player_shots = await understat.get_player_shots(
            619, {"player_assisted": "Fernandinho"})
        assert isinstance(player_shots, list)

        player_shots = await understat.get_player_shots(
            619, player_assisted="Fernandinho")
        assert isinstance(player_shots, list)

    async def test_get_matches(self, loop, understat):
        player_matches = await understat.get_player_matches(619)
        assert isinstance(player_matches, list)

        player_matches = await understat.get_player_matches(
            619, {"h_team": "Manchester United"})
        assert isinstance(player_matches, list)

        player_matches = await understat.get_player_matches(
            619, h_team="Manchester United")
        assert isinstance(player_matches, list)
