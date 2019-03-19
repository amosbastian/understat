from understat.constants import BASE_URL, LEAGUE_URL, PLAYER_URL, TEAM_URL
from understat.utils import (filter_by_positions, filter_data, get_data,
                             to_league_name)


class Understat():
    def __init__(self, session):
        self.session = session

    async def get_stats(self, options=None, **kwargs):
        """Returns a list containing stats of every league, grouped by month.

        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: List of dictionaries.
        :rtype: list
        """

        stats = await get_data(self.session, BASE_URL, "statData")

        if options:
            kwargs = options

        filtered_data = filter_data(stats, kwargs)

        return filtered_data

    async def get_teams(self, league_name, season, options=None, **kwargs):
        """Returns a list containing information about all the teams in
        the given league in the given season.

        :param league_name: The league's name.
        :type league_name: str
        :param season: The season.
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :type season: str or int
        :return: A list of the league's table as seen on Understat's
            league overview.
        :rtype: list
        """

        url = LEAGUE_URL.format(to_league_name(league_name), season)
        teams_data = await get_data(self.session, url, "teamsData")

        if options:
            kwargs = options

        filtered_data = filter_data(list(teams_data.values()), kwargs)

        return filtered_data

    async def get_league_players(
            self, league_name, season, options=None, **kwargs):
        """Returns a list containing information about all the players in
        the given league in the given season.

        :param league_name: The league's name.
        :type league_name: str
        :param season: The season.
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :type season: str or int
        :return: A list of the players as seen on Understat's league overview.
        :rtype: list
        """

        url = LEAGUE_URL.format(to_league_name(league_name), season)
        players_data = await get_data(self.session, url, "playersData")

        if options:
            kwargs = options

        filtered_data = filter_data(players_data, kwargs)

        return filtered_data

    async def get_league_results(
            self, league_name, season, options=None, **kwargs):
        """Returns a list containing information about all the results
        (matches) played by the teams in the given league in the given season.

        :param league_name: The league's name.
        :type league_name: str
        :param season: The season.
        :type season: str or int
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: A list of the results as seen on Understat's league overview.
        :rtype: list
        """

        url = LEAGUE_URL.format(to_league_name(league_name), season)
        dates_data = await get_data(self.session, url, "datesData")
        results = [r for r in dates_data if r["isResult"]]

        if options:
            kwargs = options

        filtered_data = filter_data(results, kwargs)

        return filtered_data

    async def get_league_fixtures(
            self, league_name, season,  options=None, **kwargs):
        """Returns a list containing information about all the upcoming
        fixtures of the given league in the given season.

        :param league_name: The league's name.
        :type league_name: str
        :param season: The season.
        :type season: str or int
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: A list of the fixtures as seen on Understat's league overview.
        :rtype: list
        """

        url = LEAGUE_URL.format(to_league_name(league_name), season)
        dates_data = await get_data(self.session, url, "datesData")
        fixtures = [f for f in dates_data if not f["isResult"]]

        if options:
            kwargs = options

        filtered_data = filter_data(fixtures, kwargs)

        return filtered_data

    async def get_player_shots(self, player_id, options=None, **kwargs):
        """Returns the player with the given ID's shot data.

        :param player_id: The player's Understat ID.
        :type player_id: int or str
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: List of the player's shot data.
        :rtype: list
        """

        url = PLAYER_URL.format(player_id)
        shots_data = await get_data(self.session, url, "shotsData")

        if options:
            kwargs = options

        filtered_data = filter_data(shots_data, kwargs)

        return filtered_data

    async def get_player_matches(self, player_id, options=None, **kwargs):
        """Returns the player with the given ID's matches data.

        :param player_id: The player's Understat ID.
        :type player_id: int or str
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: List of the player's matches data.
        :rtype: list
        """
        url = PLAYER_URL.format(player_id)
        matches_data = await get_data(self.session, url, "matchesData")

        if options:
            kwargs = options

        filtered_data = filter_data(matches_data, kwargs)

        return filtered_data

    async def get_player_stats(self, player_id, positions=None):
        """Returns the player with the given ID's min / max stats, per
        position(s).

        :param player_id: The player's Understat ID.
        :type player_id: int or str
        :param positions: Positions to filter the data by, defaults to None.
        :param positions: list, optional
        :return: List of the player's stats per position.
        :rtype: list
        """
        url = PLAYER_URL.format(player_id)
        player_stats = await get_data(self.session, url, "minMaxPlayerStats")

        player_stats = filter_by_positions(player_stats, positions)

        return player_stats

    async def get_player_grouped_stats(self, player_id):
        """Returns the player with the given ID's grouped stats (as seen at
        the top of a player's page).

        :param player_id: The player's Understat ID.
        :type player_id: int or str
        :return: Dictionary of the player's grouped stats.
        :rtype: dict
        """
        url = PLAYER_URL.format(player_id)
        player_stats = await get_data(self.session, url, "groupsData")

        return player_stats

    async def get_team_stats(self, team_name, season):
        """Returns a team's stats, as seen on their page on Understat, in the
        given season.

        :param team_name: A team's name, e.g. Manchester United.
        :type team_name: str
        :param season: A season / year, e.g. 2018.
        :type season: int or str
        :return: A dictionary containing a team's stats.
        :rtype: dict
        """

        url = TEAM_URL.format(team_name.replace(" ", "_"), season)
        team_stats = await get_data(self.session, url, "statisticsData")

        return team_stats

    async def get_team_results(
            self, team_name, season, options=None, **kwargs):
        """Returns a team's results in the given season.

        :param team_name: A team's name.
        :type team_name: str
        :param season: The season.
        :type season: int or str
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: List of the team's results in the given season.
        :rtype: list
        """

        url = TEAM_URL.format(team_name.replace(" ", "_"), season)
        dates_data = await get_data(self.session, url, "datesData")
        results = [r for r in dates_data if r["isResult"]]

        if options:
            kwargs = options

        filtered_data = filter_data(results, kwargs)

        return filtered_data

    async def get_team_fixtures(
            self, team_name, season, options=None, **kwargs):
        """Returns a team's upcoming fixtures in the given season.

        :param team_name: A team's name.
        :type team_name: str
        :param season: The season.
        :type season: int or str
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: List of the team's upcoming fixtures in the given season.
        :rtype: list
        """

        url = TEAM_URL.format(team_name.replace(" ", "_"), season)
        dates_data = await get_data(self.session, url, "datesData")
        fixtures = [f for f in dates_data if not f["isResult"]]

        if options:
            kwargs = options

        filtered_data = filter_data(fixtures, kwargs)

        return filtered_data

    async def get_team_players(
            self, team_name, season, options=None, **kwargs):
        """Returns a team's player statistics in the given season.

        :param team_name: A team's name.
        :type team_name: str
        :param season: The season.
        :type season: int or str
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :return: List of the team's players' statistics in the given season.
        :rtype: list
        """

        url = TEAM_URL.format(team_name.replace(" ", "_"), season)
        players_data = await get_data(self.session, url, "playersData")

        if options:
            kwargs = options

        filtered_data = filter_data(players_data, kwargs)

        return filtered_data
