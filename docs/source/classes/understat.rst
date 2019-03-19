Understat
================

.. module:: understat

The :class:`Understat <understat.Understat>` class is the main, and only class
used for interacting with Understat's data. It requires a
``aiohttp.ClientSession`` for sending requests, so typical usage of the
:class:`Understat <understat.Understat>` class can look something like this:

.. code-block:: python

    import asyncio
    import json

    import aiohttp

    from understat import Understat


    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            player = await understat.get_players(
                "epl", 2018,
                player_name="Paul Pogba",
                team_title="Manchester United"
            )
            print(json.dumps(player))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    >>>[{"id": "1740", "player_name": "Paul Pogba", "games": "27", "time": "2293", "goals": "11", "xG": "13.361832823604345", "assists": "9", "xA": "4.063152700662613", "shots": "87", "key_passes": "40", "yellow_cards": "5", "red_cards": "0", "position": "M S", "team_title": "Manchester United", "npg": "6", "npxG": "7.272482139989734", "xGChain": "17.388037759810686", "xGBuildup": "8.965998269617558"}]



.. automethod:: understat.Understat.get_fixtures

.. automethod:: understat.Understat.get_player_grouped_stats

.. automethod:: understat.Understat.get_player_matches

.. automethod:: understat.Understat.get_player_shots

.. automethod:: understat.Understat.get_player_stats

.. automethod:: understat.Understat.get_players

.. automethod:: understat.Understat.get_results

.. image:: https://i.imgur.com/5rf0ACo.png

.. automethod:: understat.Understat.get_stats

.. automethod:: understat.Understat.get_team_stats

.. automethod:: understat.Understat.get_teams