from understat.constants import LEAGUE_URL, PLAYER_URL
from understat.utils import (decode_data, fetch, filter_data, find_match,
                             get_data, to_league_name, filter_by_positions)


class Understat():
    def __init__(self, session):
        self.session = session

    async def get_teams(self, league_name, season, options=None, **kwargs):
        """Returns a list containing information about all the teams in
        the given league in the given season.

        :param league_name: The league's name.
        :type league_name: str
        :param season: The season.
        :param options: Options to filter the data by, defaults to None.
        :param options: dict, optional
        :type season: str or int
        :return: A dictionary of the league's table as seen on Understat's
            league overview.
        :rtype: list
        """

        url = LEAGUE_URL.format(to_league_name(league_name), season)
        teams_data = await get_data(self.session, url, "teamsData")

        if options:
            kwargs = options

        filtered_data = filter_data(list(teams_data.values()), kwargs)

        return filtered_data

    async def get_players(self, league_name, season, options=None, **kwargs):
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

    async def get_results(self, league_name, season, options=None, **kwargs):
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

    async def get_fixtures(self, league_name, season,  options=None, **kwargs):
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

        return shots_data

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

        if positions:
            player_stats = filter_by_positions(player_stats, positions)

        return player_stats
