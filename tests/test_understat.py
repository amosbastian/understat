import aiohttp

from understat import Understat

leagues = ["epl", "la_liga", "bundesliga", "serie_a", "ligue_1", "rfpl"]


class TestUnderstat(object):
    async def test_init(self, loop):
        session = aiohttp.ClientSession()
        understat = Understat(session)
        assert understat.session is session
        await session.close()

    async def test_get_stats(self, loop, understat):
        stats = await understat.get_stats()
        assert isinstance(stats, list)

    async def test_get_stats_with_options(self, loop, understat):
        stats = await understat.get_stats(league="EPL")
        assert isinstance(stats, list)

        stats = await understat.get_stats({"league": "EPL", "month": "8"})
        assert isinstance(stats, list)

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

    async def test_get_league_players(self, loop, understat):
        for league in leagues:
            players = await understat.get_league_players(league, 2018)
            assert isinstance(players, list)

    async def test_get_league_players_with_options(self, loop, understat):
        player = await understat.get_league_players(
            "epl", 2018, player_name="Paul Pogba",
            team_title="Manchester United")
        assert isinstance(player, list)
        assert len(player) == 1

        player = await understat.get_league_players(
            "epl", 2018, {"position": "F S",
                          "yellow_cards": "3",
                          "player_name": "Sergio Agüero"})
        assert isinstance(player, list)
        assert len(player) == 1

        player = await understat.get_league_players(
            "epl", 2018, player_name="Lionel Messi")
        assert isinstance(player, list)
        assert not player

    async def test_get_league_results(self, loop, understat):
        for league in leagues:
            results = await understat.get_league_results(league, 2018)
            assert isinstance(results, list)

        for result in results:
            assert result["isResult"]

    async def test_get_league_results_with_options(self, loop, understat):
        results = await understat.get_league_results("epl", 2018, {
            "h": {"id": "89",
                  "title": "Manchester United",
                  "short_title": "MUN"}
        })
        assert isinstance(results, list)
        assert len(results) > 0

        results_without_option = await understat.get_league_results(
            "epl", 2018, isResult=True)
        results_with_option = await understat.get_league_results(
            "epl", 2018, isResult=True)
        assert results_with_option == results_without_option

    async def test_get_league_fixtures(self, loop, understat):
        for league in leagues:
            fixtures = await understat.get_league_fixtures(league, 2018)
            assert isinstance(fixtures, list)

        for fixture in fixtures:
            assert not fixture["isResult"]

    async def test_get_league_fixtures_with_options(self, loop, understat):
        results = await understat.get_league_fixtures("epl", 2024, {
            "h": {"id": "89",
                  "title": "Manchester United",
                  "short_title": "MUN"}
        })
        assert isinstance(results, list)
        assert results

    async def test_get_league_table(self, loop, understat):
        table = await understat.get_league_table("epl", 2020)
        assert isinstance(table, list)

    async def test_get_league_table_with_date(self, loop, understat):
        table = await understat.get_league_table("epl", 2020, start_date="2020-11-01", end_date="2021-01-31")
        assert isinstance(table, list)

    async def test_get_player_shots(self, loop, understat):
        player_shots = await understat.get_player_shots(619)
        assert isinstance(player_shots, list)

    async def test_get_player_shots_with_options(self, loop, understat):
        player_shots = await understat.get_player_shots(
            619, {"player_assisted": "Fernandinho"})
        assert isinstance(player_shots, list)

        player_shots = await understat.get_player_shots(
            619, player_assisted="Fernandinho")
        assert isinstance(player_shots, list)

    async def test_get_matches(self, loop, understat):
        player_matches = await understat.get_player_matches(619)
        assert isinstance(player_matches, list)

    async def test_get_matches_with_options(self, loop, understat):
        player_matches = await understat.get_player_matches(
            619, {"h_team": "Manchester United"})
        assert isinstance(player_matches, list)

        player_matches = await understat.get_player_matches(
            619, h_team="Manchester United")
        assert isinstance(player_matches, list)

    async def test_get_player_stats(self, loop, understat):
        player_stats = await understat.get_player_stats(619)
        assert isinstance(player_stats, list)
        assert len(player_stats) > 1

        player_stats = await understat.get_player_stats(619, ["FW"])
        assert isinstance(player_stats, list)
        assert len(player_stats) == 1

    async def test_get_player_grouped_stats(self, loop, understat):
        grouped_stats = await understat.get_player_grouped_stats(619)
        assert isinstance(grouped_stats, dict)

    async def test_get_team_stats(self, loop, understat):
        team_stats = await understat.get_team_stats("Manchester United", 2018)
        assert isinstance(team_stats, dict)

    async def test_get_team_results(self, loop, understat):
        results = await understat.get_team_results("Manchester United", 2018)
        assert isinstance(results, list)

    async def test_get_team_results_with_options(self, loop, understat):
        results = await understat.get_team_results(
            "Manchester United", 2018, side="h")
        assert isinstance(results, list)

        results = await understat.get_team_results(
            "Manchester United", 2018, {"side": "h", "result": "w"})
        assert isinstance(results, list)

    async def test_get_team_fixtures(self, loop, understat):
        fixtures = await understat.get_team_fixtures("Manchester United", 2018)
        assert isinstance(fixtures, list)

    async def test_get_team_fixtures_with_options(self, loop, understat):
        fixtures = await understat.get_team_fixtures(
            "Manchester United", 2018, side="h")
        assert isinstance(fixtures, list)

        fixtures = await understat.get_team_fixtures(
            "Manchester United", 2018, {"side": "h", "result": "w"})
        assert isinstance(fixtures, list)

    async def test_get_team_players(self, loop, understat):
        players = await understat.get_team_players("Manchester United", 2018)
        assert isinstance(players, list)

    async def test_get_team_players_with_options(self, loop, understat):
        players = await understat.get_team_players(
            "Manchester United", 2018, position="F S")
        assert isinstance(players, list)

        players = await understat.get_team_players(
            "Manchester United", 2018, {"position": "F S", "red_cards": "0"})
        assert isinstance(players, list)

    async def test_get_match_stats(self, loop, understat):
        stats = await understat.get_match_stats(11670)
        assert isinstance(stats, dict)

    async def test_get_match_players(self, loop, understat):
        players = await understat.get_match_players(11670)
        assert isinstance(players, dict)
        assert isinstance(players["h"], dict)
        assert isinstance(players["a"], dict)

    async def test_get_match_shots(self, loop, understat):
        shots = await understat.get_match_shots(11670)
        assert isinstance(shots, dict)
        assert isinstance(shots["h"], list)
        assert isinstance(shots["a"], list)
