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

The functions
-------------

Below each function of the :class:`Understat <understat.Understat>` class will
be documented separately. It will also show a screenshot of the equivalent data
on `understat.com <https://understat.com>`_, and an example of how the function
itself could be used.

---

.. automethod:: understat.Understat.get_fixtures

It returns the fixtures (not results) of the given league, in the given season.
So for example, the fixtures as seen in the screenshot below

.. image:: https://i.imgur.com/dE54ox0.png

An example of getting all Manchester United's upcoming fixtures is given below

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            fixtures = await understat.get_fixtures("epl", 2018, {
                "h": {"id": "89",
                    "title": "Manchester United",
                    "short_title": "MUN"}
            })
            print(json.dumps(fixtures))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which prints

.. code-block:: javascript

    [
        {
            "id": "9501",
            "isResult": false,
            "h": {
            "id": "89",
            "title": "Manchester United",
            "short_title": "MUN"
            },
            "a": {
            "id": "88",
            "title": "Manchester City",
            "short_title": "MCI"
            },
            "goals": {
            "h": null,
            "a": null
            },
            "xG": {
            "h": null,
            "a": null
            },
            "datetime": "2019-03-16 18:00:00"
        },
        ...
        {
            "id": "9570",
            "isResult": false,
            "h": {
            "id": "89",
            "title": "Manchester United",
            "short_title": "MUN"
            },
            "a": {
            "id": "227",
            "title": "Cardiff",
            "short_title": "CAR"
            },
            "goals": {
            "h": null,
            "a": null
            },
            "xG": {
            "h": null,
            "a": null
            },
            "datetime": "2019-05-12 17:00:00"
        }
    ]

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