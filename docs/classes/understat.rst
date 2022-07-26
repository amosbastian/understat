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
            player = await understat.get_league_players(
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

Most of the functions come with the `options` keyword argument, and the
`**kwargs` magic variable, which means that their output can be filtered
(the ways this can be done depends entirely on the output). It was the easiest
way to implement something like this, but may not always be optimal (e.g.
filtering by home team may require an object for example), and so this could be
changed in the future.

If you have any suggestions on what kind of filtering
options you'd like to see for certain functions, then you can create an
`issue <https://github.com/amosbastian/understat/issues>`_ for this. Also, any
help with adding better filtering, if necessary, is also very much appreciated!

---

.. automethod:: understat.Understat.get_league_fixtures

It returns the fixtures (not results) of the given league, in the given season.
So for example, the fixtures as seen in the screenshot below

.. image:: https://i.imgur.com/dE54ox0.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output.
So for example, if you wanted to get all Manchester United's upcoming fixtures
at **home**, then you could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            fixtures = await understat.get_league_fixtures(
                "epl",
                2018,
                {
                    "h": {"id": "89",
                          "title": "Manchester United",
                          "short_title": "MUN"}
                }
            )
            print(json.dumps(fixtures))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

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

---

.. automethod:: understat.Understat.get_league_table

It returns the standings of the given league in the given year, as seen in the screenshot below

.. image:: https://i.imgur.com/fYo9zkz.png

There are also optional "start_date" and "end_date" arguments,
which can be used to get the table from a specific date range from given season, like on screenshot below

.. image:: https://i.imgur.com/r30bdpn.png

An example of getting the standings from the EPL in 2019 can be found below

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            table = await understat.get_league_table("EPL", "2019")
            print(table)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    [
     ['Team', 'M', 'W', 'D', 'L', 'G', 'GA', 'PTS', 'xG', 'NPxG', 'xGA', 'NPxGA', 'NPxGD', 'PPDA', 'OPPDA', 'DC', 'ODC', 'xPTS'],
     ['Liverpool', 38, 32, 3, 3, 85, 33, 99, 75.19, 71.39, 39.57, 38.81, 32.58, 8.01, 21.33, 429, 145, 74.28],
     ['Manchester City', 38, 26, 3, 9, 102, 35, 81, 102.21, 93.53, 37.0, 34.71, 58.82, 8.49, 23.77, 547, 135, 86.76],
     ['Manchester United', 38, 18, 12, 8, 66, 36, 66, 66.19, 55.53, 38.06, 35.78, 19.75, 9.64, 11.1, 290, 178, 70.99],
     ...,
     ['Aston Villa', 38, 9, 8, 21, 41, 67, 35, 45.09, 42.65, 71.6, 66.88, -24.23, 12.34, 7.89, 186, 343, 37.23],
     ['Bournemouth', 38, 9, 7, 22, 40, 65, 34, 44.67, 41.63, 63.29, 58.73, -17.1, 13.38, 9.15, 210, 326, 39.2],
     ['Watford', 38, 8, 10, 20, 36, 64, 34, 48.56, 42.47, 59.53, 52.52, -10.05, 12.2, 9.64, 227, 259, 47.87],
     ['Norwich', 38, 5, 6, 27, 26, 75, 21, 37.23, 35.71, 71.61, 66.13, -30.41, 12.59, 9.65, 207, 345, 33.12]
    ]

---

.. automethod:: understat.Understat.get_player_grouped_stats

It returns all the statistics of a given player, which includes stuff like
their performance per season, position and more. Basically, it's everything
that can be found in the table shown in the screenshot below

.. image:: https://i.imgur.com/gEMSKin.png

An example of getting Sergio Agüero's grouped data can be found below

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            grouped_stats = await understat.get_player_grouped_stats(619)
            print(json.dumps(grouped_stats))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    {
        "season": [
            {
            "position": "FW",
            "games": "26",
            "goals": "18",
            "shots": "95",
            "time": "1960",
            "xG": "17.515484783798456",
            "assists": "6",
            "xA": "3.776376834139228",
            "key_passes": "25",
            "season": "2018",
            "team": "Manchester City",
            "yellow": "3",
            "red": "0",
            "npg": "16",
            "npxG": "15.9931472055614",
            "xGChain": "23.326821692287922",
            "xGBuildup": "6.351545065641403"
            },
            ...,
            {
            "position": "Sub",
            "games": "33",
            "goals": "26",
            "shots": "148",
            "time": "2551",
            "xG": "25.270159743726254",
            "assists": "8",
            "xA": "5.568922242149711",
            "key_passes": "33",
            "season": "2014",
            "team": "Manchester City",
            "yellow": "4",
            "red": "0",
            "npg": "21",
            "npxG": "20.70318364351988",
            "xGChain": "27.805154908448458",
            "xGBuildup": "6.878173082135618"
            }
        ],
        "position": {
            "2018": {
                "FW": {
                    "position": "FW",
                    "games": "24",
                    "goals": "18",
                    "shots": "94",
                    "time": "1911",
                    "xG": "17.464063242077827",
                    "assists": "6",
                    "xA": "3.776376834139228",
                    "key_passes": "25",
                    "season": "2018",
                    "yellow": "3",
                    "red": "0",
                    "npg": "16",
                    "npxG": "15.94172566384077",
                    "xGChain": "23.258203461766243",
                    "xGBuildup": "6.334348376840353"
                },
                "Sub": {
                    "position": "Sub",
                    "games": "2",
                    "goals": "0",
                    "shots": "1",
                    "time": "49",
                    "xG": "0.05142154172062874",
                    "assists": "0",
                    "xA": "0",
                    "key_passes": "0",
                    "season": "2018",
                    "yellow": "0",
                    "red": "0",
                    "npg": "0",
                    "npxG": "0.05142154172062874",
                    "xGChain": "0.06861823052167892",
                    "xGBuildup": "0.017196688801050186"
                }
            },
            ...,
            },
            "2014": {
                "FW": {
                    "position": "FW",
                    "games": "30",
                    "goals": "24",
                    "shots": "142",
                    "time": "2504",
                    "xG": "24.362012460827827",
                    "assists": "8",
                    "xA": "5.568922242149711",
                    "key_passes": "33",
                    "season": "2014",
                    "yellow": "4",
                    "red": "0",
                    "npg": "19",
                    "npxG": "19.795036360621452",
                    "xGChain": "26.94415594637394",
                    "xGBuildup": "6.878173082135618"
                },
                "Sub": {
                    "position": "Sub",
                    "games": "3",
                    "goals": "2",
                    "shots": "6",
                    "time": "47",
                    "xG": "0.9081472828984261",
                    "assists": "0",
                    "xA": "0",
                    "key_passes": "0",
                    "season": "2014",
                    "yellow": "0",
                    "red": "0",
                    "npg": "2",
                    "npxG": "0.9081472828984261",
                    "xGChain": "0.8609989620745182",
                    "xGBuildup": "0"
                }
            }
        },
        "situation": {
            "2015": {
                "OpenPlay": {
                    "situation": "OpenPlay",
                    "season": "2015",
                    "goals": "17",
                    "shots": "97",
                    "xG": "13.971116883680224",
                    "assists": "2",
                    "key_passes": "26",
                    "xA": "2.0287596937268972",
                    "npg": "17",
                    "npxG": "13.971116883680224",
                    "time": 2399
                },
                "FromCorner": {
                    "situation": "FromCorner",
                    "season": "2015",
                    "goals": "2",
                    "shots": "11",
                    "xG": "1.8276203628629446",
                    "assists": "0",
                    "key_passes": "0",
                    "xA": "0",
                    "npg": "2",
                    "npxG": "1.8276203628629446",
                    "time": 2399
                },
                "Penalty": {
                    "situation": "Penalty",
                    "season": "2015",
                    "goals": "4",
                    "shots": "5",
                    "xG": "3.8058441877365112",
                    "assists": "0",
                    "key_passes": "0",
                    "xA": "0",
                    "npg": "0",
                    "npxG": "0",
                    "time": 2399
            },
            ...,
            "2014": {
                "OpenPlay": {
                    "situation": "OpenPlay",
                    "season": "2014",
                    "goals": "19",
                    "shots": "128",
                    "xG": "18.23446972388774",
                    "assists": "7",
                    "key_passes": "32",
                    "xA": "4.622839629650116",
                    "npg": "19",
                    "npxG": "18.23446972388774",
                    "time": 2551
                },
                "FromCorner": {
                    "situation": "FromCorner",
                    "season": "2014",
                    "goals": "1",
                    "shots": "12",
                    "xG": "1.8788630235940218",
                    "assists": "1",
                    "key_passes": "1",
                    "xA": "0.9460826516151428",
                    "npg": "1",
                    "npxG": "1.8788630235940218",
                    "time": 2551
                },
                "Penalty": {
                    "situation": "Penalty",
                    "season": "2014",
                    "goals": "5",
                    "shots": "6",
                    "xG": "4.566976249217987",
                    "assists": "0",
                    "key_passes": "0",
                    "xA": "0",
                    "npg": "0",
                    "npxG": "0",
                    "time": 2551
                },
                "SetPiece": {
                    "situation": "SetPiece",
                    "season": "2014",
                    "goals": "1",
                    "shots": "2",
                    "xG": "0.5898510366678238",
                    "assists": "0",
                    "key_passes": "0",
                    "xA": "0",
                    "npg": "1",
                    "npxG": "0.5898510366678238",
                    "time": 2551
                }
            }
        },
        "shotZones": {
            "2014": {
                "shotOboxTotal": {
                    "shotZones": "shotOboxTotal",
                    "season": "2014",
                    "goals": "2",
                    "shots": "33",
                    "xG": "1.5900825830176473",
                    "assists": "2",
                    "key_passes": "9",
                    "xA": "0.3100438117980957",
                    "npg": "2",
                    "npxG": "1.5900825830176473"
                },
                "shotPenaltyArea": {
                    "shotZones": "shotPenaltyArea",
                    "season": "2014",
                    "goals": "22",
                    "shots": "108",
                    "xG": "19.79369100742042",
                    "assists": "5",
                    "key_passes": "22",
                    "xA": "3.9576267898082733",
                    "npg": "17",
                    "npxG": "15.226714758202434"
                },
                "shotSixYardBox": {
                    "shotZones": "shotSixYardBox",
                    "season": "2014",
                    "goals": "2",
                    "shots": "7",
                    "xG": "3.8863864429295063",
                    "assists": "1",
                    "key_passes": "2",
                    "xA": "1.3012516796588898",
                    "npg": "2",
                    "npxG": "3.8863864429295063"
                }
            },
            ...,
            "2018": {
                "shotOboxTotal": {
                    "shotZones": "shotOboxTotal",
                    "season": "2018",
                    "goals": "2",
                    "shots": "21",
                    "xG": "0.8707829182967544",
                    "assists": "1",
                    "key_passes": "9",
                    "xA": "0.31408058758825064",
                    "npg": "2",
                    "npxG": "0.8707829182967544"
                },
                "shotPenaltyArea": {
                    "shotZones": "shotPenaltyArea",
                    "season": "2018",
                    "goals": "12",
                    "shots": "65",
                    "xG": "11.844964944757521",
                    "assists": "4",
                    "key_passes": "14",
                    "xA": "2.1070052348077297",
                    "npg": "10",
                    "npxG": "10.322627269662917"
                },
                "shotSixYardBox": {
                    "shotZones": "shotSixYardBox",
                    "season": "2018",
                    "goals": "4",
                    "shots": "9",
                    "xG": "4.799736991524696",
                    "assists": "1",
                    "key_passes": "2",
                    "xA": "1.3552910089492798",
                    "npg": "4",
                    "npxG": "4.799736991524696"
                }
            }
        },
        "shotTypes": {
            "2014": {
                "RightFoot": {
                    "shotTypes": "RightFoot",
                    "season": "2014",
                    "goals": "18",
                    "shots": "96",
                    "xG": "17.13349057827145",
                    "assists": "5",
                    "key_passes": "19",
                    "xA": "3.883937703445554",
                    "npg": "13",
                    "npxG": "12.566514329053462"
                },
                "LeftFoot": {
                    "shotTypes": "LeftFoot",
                    "season": "2014",
                    "goals": "7",
                    "shots": "40",
                    "xG": "6.236775731667876",
                    "assists": "3",
                    "key_passes": "13",
                    "xA": "1.6454832945019007",
                    "npg": "7",
                    "npxG": "6.236775731667876"
                },
                "Head": {
                    "shotTypes": "Head",
                    "season": "2014",
                    "goals": "1",
                    "shots": "12",
                    "xG": "1.8998937234282494",
                    "assists": "0",
                    "key_passes": "1",
                    "xA": "0.03950128331780434",
                    "npg": "1",
                    "npxG": "1.8998937234282494"
                }
            },
            ...,
            },
            "2018": {
                "RightFoot": {
                    "shotTypes": "RightFoot",
                    "season": "2018",
                    "goals": "9",
                    "shots": "58",
                    "xG": "9.876922971569002",
                    "assists": "3",
                    "key_passes": "9",
                    "xA": "1.6752301333472133",
                    "npg": "7",
                    "npxG": "8.354585296474397"
                },
                "LeftFoot": {
                    "shotTypes": "LeftFoot",
                    "season": "2018",
                    "goals": "6",
                    "shots": "26",
                    "xG": "4.921279687434435",
                    "assists": "3",
                    "key_passes": "16",
                    "xA": "2.101146697998047",
                    "npg": "6",
                    "npxG": "4.921279687434435"
                },
                "Head": {
                    "shotTypes": "Head",
                    "season": "2018",
                    "goals": "2",
                    "shots": "10",
                    "xG": "1.8183354930952191",
                    "assists": "0",
                    "key_passes": "0",
                    "xA": "0",
                    "npg": "2",
                    "npxG": "1.8183354930952191"
                },
                "OtherBodyPart": {
                    "shotTypes": "OtherBodyPart",
                    "season": "2018",
                    "goals": "1",
                    "shots": "1",
                    "xG": "0.8989467024803162",
                    "assists": "0",
                    "key_passes": "0",
                    "xA": "0",
                    "npg": "1",
                    "npxG": "0.8989467024803162"
                }
            }
        }
    }

---

.. automethod:: understat.Understat.get_player_matches

It returns the information about the matches played by the given player. So for
example, the matches Sergio Agüero has played, as seen in the screenshot

.. image:: https://i.imgur.com/p7jh1mh.png

This function also comes with the `options` keyword argument, and also the
`**kwargs` magic variable. An example of how you could
use either of these to filter Sergio Agüero's matches to only include matches
where Manchester United were the home team is shown below

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            # Using **kwargs
            player_matches = await understat.get_player_matches(
                619, h_team="Manchester United")
            # Or using options keyword arugment
            player_matches = await understat.get_player_matches(
                619, {"h_team": "Manchester United"})
            print(json.dumps(player_matches))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs

.. code-block:: javascript

    [
        {
            "goals": "2",
            "shots": "5",
            "xG": "1.4754852056503296",
            "time": "90",
            "position": "FW",
            "h_team": "Manchester United",
            "a_team": "Manchester City",
            "h_goals": "4",
            "a_goals": "2",
            "date": "2015-04-12",
            "id": "4459",
            "season": "2014",
            "roster_id": "23306",
            "xA": "0",
            "assists": "0",
            "key_passes": "0",
            "npg": "2",
            "npxG": "1.4754852056503296",
            "xGChain": "1.4855852127075195",
            "xGBuildup": "0.04120262712240219"
        }
    ]

Since the usage of both the `options` keyword argument and the `**kwargs` magic
variable have been shown, the examples following this will only show *one* of
the two.

---

.. automethod:: understat.Understat.get_player_shots

It returns the given player's shot data, which includes information about the
situation (open play, freekick etc.), if it hit the post or was a goal, and
more. Basically, all the information that you can get from a player's page in
the section shown below

.. image:: https://i.imgur.com/t80WF5r.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. So for example,
if you wanted to get all Sergio Agüero's shots (not necessarily goals) that
were assisted by Fernandinho, then you could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            player_shots = await understat.get_player_shots(
                619, {"player_assisted": "Fernandinho"})
            print(json.dumps(player_shots))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    [
        {
            "id": "14552",
            "minute": "91",
            "result": "SavedShot",
            "X": "0.9259999847412109",
            "Y": "0.6809999847412109",
            "xG": "0.0791548416018486",
            "player": "Sergio Ag\u00fcero",
            "h_a": "a",
            "player_id": "619",
            "situation": "OpenPlay",
            "season": "2014",
            "shotType": "LeftFoot",
            "match_id": "4757",
            "h_team": "Newcastle United",
            "a_team": "Manchester City",
            "h_goals": "0",
            "a_goals": "2",
            "date": "2014-08-17 16:00:00",
            "player_assisted": "Fernandinho",
            "lastAction": "Pass"
        },
        ...,
        {
            "id": "233670",
            "minute": "15",
            "result": "MissedShots",
            "X": "0.7419999694824219",
            "Y": "0.5359999847412109",
            "xG": "0.029104366898536682",
            "player": "Sergio Ag\u00fcero",
            "h_a": "h",
            "player_id": "619",
            "situation": "OpenPlay",
            "season": "2018",
            "shotType": "RightFoot",
            "match_id": "9234",
            "h_team": "Manchester City",
            "a_team": "Newcastle United",
            "h_goals": "2",
            "a_goals": "1",
            "date": "2018-09-01 16:30:00",
            "player_assisted": "Fernandinho",
            "lastAction": "Pass"
        }
    ]

---

.. automethod:: understat.Understat.get_player_stats

It returns the player's average stats overall, which includes stuff like their
average goals per 90 minutes, average expected assists per 90 minutes and more.
Basically everything you can see on a player's page in the section shown below

.. image:: https://i.imgur.com/uJ2o0zi.png

The function comes with the `positions` argument, which can be used to filter
the stats by position(s). So for example, if you wanted to get Sergio Agüero's
performance as a forward, then you could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            player_stats = await understat.get_player_stats(619, ["FW"])
            print(json.dumps(player_stats))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs

.. code-block:: javascript

    [
        {
            "goals": {
            "min": 0.0011,
            "max": 0.0126,
            "avg": 0.0042
            },
            "xG": {
            "min": 0.00172821,
            "max": 0.0120816,
            "avg": 0.00415549
            },
            "shots": {
            "min": 0.015,
            "max": 0.0737,
            "avg": 0.028
            },
            "assists": {
            "min": 0,
            "max": 0.0048,
            "avg": 0.0014
            },
            "xA": {
            "min": 0.000264191,
            "max": 0.00538174,
            "avg": 0.00131568
            },
            "key_passes": {
            "min": 0.0036,
            "max": 0.0309,
            "avg": 0.012
            },
            "xGChain": {
            "min": 0.00272705,
            "max": 0.0169137,
            "avg": 0.00533791
            },
            "xGBuildup": {
            "min": 0.000243189,
            "max": 0.00671256,
            "avg": 0.00131848
            },
            "position": "FW"
        }
    ]

---

.. automethod:: understat.Understat.get_league_players

It returns all the information about the players in a given league in the given
season. This includes stuff like their number of goals scored, their total
expected assists and more. Basically, it's all the information you can find
in the player table shown on all league overview pages on
`understat.com <https://understat.com>`_.

.. image:: https://i.imgur.com/vPJzqnd.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. So for example,
if you wanted to get all the players who play for Manchester United, then you
could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            players = await understat.get_league_players(
                "epl",
                2018,
                team_title="Manchester United"
            )
            print(json.dumps(players))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    [
        {
            "id": "594",
            "player_name": "Romelu Lukaku",
            "games": "27",
            "time": "1768",
            "goals": "12",
            "xG": "12.054240763187408",
            "assists": "0",
            "xA": "1.6836179178208113",
            "shots": "50",
            "key_passes": "17",
            "yellow_cards": "4",
            "red_cards": "0",
            "position": "F S",
            "team_title": "Manchester United",
            "npg": "12",
            "npxG": "12.054240763187408",
            "xGChain": "12.832402393221855",
            "xGBuildup": "3.366600174456835"
        },
        ...,
        {
            "id": "1740",
            "player_name": "Paul Pogba",
            "games": "27",
            "time": "2293",
            "goals": "11",
            "xG": "13.361832823604345",
            "assists": "9",
            "xA": "4.063152700662613",
            "shots": "87",
            "key_passes": "40",
            "yellow_cards": "5",
            "red_cards": "0",
            "position": "M S",
            "team_title": "Manchester United",
            "npg": "6",
            "npxG": "7.272482139989734",
            "xGChain": "17.388037759810686",
            "xGBuildup": "8.965998269617558"
        }
    ]

---

.. automethod:: understat.Understat.get_league_results

It returns the results (not fixtures) of the given league, in the given season.
So for example, the results as seen in the screenshot below

.. image:: https://i.imgur.com/LyWGAJw.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. So for example,
if you wanted to get all Manchester United's results away from home, then you
could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            fixtures = await understat.get_league_results(
                "epl",
                2018,
                {
                    "a": {"id": "89",
                        "title": "Manchester United",
                        "short_title": "MUN"}
                }
            )
            print(json.dumps(fixtures))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    [
        {
            "id": "9215",
            "isResult": true,
            "h": {
                "id": "220",
                "title": "Brighton",
                "short_title": "BRI"
            },
            "a": {
                "id": "89",
                "title": "Manchester United",
                "short_title": "MUN"
            },
            "goals": {
                "h": "3",
                "a": "2"
            },
            "xG": {
                "h": "1.63672",
                "a": "1.56579"
            },
            "datetime": "2018-08-19 18:00:00",
            "forecast": {
                "w": "0.3538",
                "d": "0.3473",
                "l": "0.2989"
            }
        },
        ...,
        {
            "id": "9496",
            "isResult": true,
            "h": {
                "id": "83",
                "title": "Arsenal",
                "short_title": "ARS"
            },
            "a": {
                "id": "89",
                "title": "Manchester United",
                "short_title": "MUN"
            },
            "goals": {
                "h": "2",
                "a": "0"
            },
            "xG": {
                "h": "1.52723",
                "a": "2.3703"
            },
            "datetime": "2019-03-10 16:30:00",
            "forecast": {
                "w": "0.1667",
                "d": "0.227",
                "l": "0.6063"
            }
        }
    ]

---

.. automethod:: understat.Understat.get_match_players

It returns information about the players who played in the given match.
So for example, the players seen in the screenshot below

.. image:: https://i.imgur.com/b7etgfp.png

An example of getting the players who played in the match between Manchester
United and Chelsea on 11 August, 2019 which ended 4-0 can be seen below:

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            players = await understat.get_match_players(11652)
            print(json.dumps(players))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    {
        "h": {
            "341628": {
                "id": "341628",
                "goals": "2",
                "own_goals": "0",
                "shots": "4",
                "xG": "1.3030972480773926",
                "time": "88",
                "player_id": "556",
                "team_id": "89",
                "position": "AML",
                "player": "Marcus Rashford",
                "h_a": "h",
                "yellow_card": "0",
                "red_card": "0",
                "roster_in": "341631",
                "roster_out": "0",
                "key_passes": "0",
                "assists": "0",
                "xA": "0",
                "xGChain": "1.1517746448516846",
                "xGBuildup": "0.6098462343215942",
                "positionOrder": "13"
            },
            ...,
            "341629": {
                "id": "341629",
                "goals": "1",
                "own_goals": "0",
                "shots": "4",
                "xG": "0.7688590884208679",
                "time": "90",
                "player_id": "553",
                "team_id": "89",
                "position": "FW",
                "player": "Anthony Martial",
                "h_a": "h",
                "yellow_card": "1",
                "red_card": "0",
                "roster_in": "0",
                "roster_out": "0",
                "key_passes": "1",
                "assists": "0",
                "xA": "0.05561231076717377",
                "xGChain": "0.9395027160644531",
                "xGBuildup": "0.11503136157989502",
                "positionOrder": "15"
            }
        },
        "a": {
            "341633": {
                "id": "341633",
                "goals": "0",
                "own_goals": "0",
                "shots": "0",
                "xG": "0",
                "time": "90",
                "player_id": "5061",
                "team_id": "80",
                "position": "GK",
                "player": "Kepa",
                "h_a": "a",
                "yellow_card": "0",
                "red_card": "0",
                "roster_in": "0",
                "roster_out": "0",
                "key_passes": "0",
                "assists": "0",
                "xA": "0",
                "xGChain": "0.04707280918955803",
                "xGBuildup": "0.04707280918955803",
                "positionOrder": "1"
            },
            ...,
            "341642": {
                "id": "341642",
                "goals": "0",
                "own_goals": "0",
                "shots": "2",
                "xG": "0.08609434962272644",
                "time": "60",
                "player_id": "592",
                "team_id": "80",
                "position": "AML",
                "player": "Ross Barkley",
                "h_a": "a",
                "yellow_card": "0",
                "red_card": "0",
                "roster_in": "341646",
                "roster_out": "0",
                "key_passes": "1",
                "assists": "0",
                "xA": "0.024473881348967552",
                "xGChain": "0.11056823283433914",
                "xGBuildup": "0",
                "positionOrder": "13"
            }
        }
    }

---

.. automethod:: understat.Understat.get_match_shots

It returns information about the shots made by players who played in the given
match. So for example, the shots seen in the screenshot below

.. image:: https://i.imgur.com/3z5wkAV.png

An example of getting the shots made in the match between Manchester United and
Chelsea on 11 August, 2019 which ended 4-0 can be seen below:

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            players = await understat.get_match_shots(11652)
            print(json.dumps(players))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    {
        "h": [
            {
                "id": "310295",
                "minute": "6",
                "result": "SavedShot",
                "X": "0.8280000305175781",
                "Y": "0.639000015258789",
                "xG": "0.04247729107737541",
                "player": "Anthony Martial",
                "h_a": "h",
                "player_id": "553",
                "situation": "OpenPlay",
                "season": "2019",
                "shotType": "RightFoot",
                "match_id": "11652",
                "h_team": "Manchester United",
                "a_team": "Chelsea",
                "h_goals": "4",
                "a_goals": "0",
                "date": "2019-08-11 16:30:00",
                "player_assisted": null,
                "lastAction": "None"
            },
            ...,
            {
                "id": "310318",
                "minute": "86",
                "result": "BlockedShot",
                "X": "0.8669999694824219",
                "Y": "0.47299999237060547",
                "xG": "0.11503136157989502",
                "player": "Mason Greenwood",
                "h_a": "h",
                "player_id": "7490",
                "situation": "OpenPlay",
                "season": "2019",
                "shotType": "RightFoot",
                "match_id": "11652",
                "h_team": "Manchester United",
                "a_team": "Chelsea",
                "h_goals": "4",
                "a_goals": "0",
                "date": "2019-08-11 16:30:00",
                "player_assisted": "Aaron Wan-Bissaka",
                "lastAction": "Cross"
            }
        ],
        "a": [
            {
                "id": "310293",
                "minute": "3",
                "result": "ShotOnPost",
                "X": "0.835999984741211",
                "Y": "0.38599998474121094",
                "xG": "0.03392893448472023",
                "player": "Tammy Abraham",
                "h_a": "a",
                "player_id": "702",
                "situation": "FromCorner",
                "season": "2019",
                "shotType": "RightFoot",
                "match_id": "11652",
                "h_team": "Manchester United",
                "a_team": "Chelsea",
                "h_goals": "4",
                "a_goals": "0",
                "date": "2019-08-11 16:30:00",
                "player_assisted": "Mateo Kovacic",
                "lastAction": "BallTouch"
            },
            ...,
            {
                "id": "310321",
                "minute": "93",
                "result": "SavedShot",
                "X": "0.850999984741211",
                "Y": "0.7",
                "xG": "0.043492574244737625",
                "player": "Emerson",
                "h_a": "a",
                "player_id": "1245",
                "situation": "OpenPlay",
                "season": "2019",
                "shotType": "LeftFoot",
                "match_id": "11652",
                "h_team": "Manchester United",
                "a_team": "Chelsea",
                "h_goals": "4",
                "a_goals": "0",
                "date": "2019-08-11 16:30:00",
                "player_assisted": "Christian Pulisic",
                "lastAction": "Pass"
            }
        ]
    }

---

.. automethod:: understat.Understat.get_stats

It returns the average stats of all the leagues tracked on
`understat.com <https://understat.com>`_, split by month. Basically, it is all
the information you see on their homepage, as seen in the screenshot below

.. image:: https://i.imgur.com/5rf0ACo.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. So for example,
if you wanted to gets the stats for the Premier League in the 8th month of each
year they have been tracking the stats, then you could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            stats = await understat.get_stats({"league": "EPL", "month": "8"})
            print(json.dumps(stats))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs

.. code-block:: javascript

    [
        {
            "league_id": "1",
            "league": "EPL",
            "h": "1.3000",
            "a": "1.4000",
            "hxg": "1.141921697060267",
            "axg": "1.110964298248291",
            "year": "2014",
            "month": "8",
            "matches": "30"
        },
        {
            "league_id": "1",
            "league": "EPL",
            "h": "1.1000",
            "a": "1.3750",
            "hxg": "1.2151590750552714",
            "axg": "1.221375621855259",
            "year": "2015",
            "month": "8",
            "matches": "40"
        },
        {
            "league_id": "1",
            "league": "EPL",
            "h": "1.2000",
            "a": "1.2000",
            "hxg": "1.3605596815546355",
            "axg": "1.145853524406751",
            "year": "2016",
            "month": "8",
            "matches": "30"
        },
        {
            "league_id": "1",
            "league": "EPL",
            "h": "1.3000",
            "a": "1.1333",
            "hxg": "1.4422248949607213",
            "axg": "1.096401752779881",
            "year": "2017",
            "month": "8",
            "matches": "30"
        },
        {
            "league_id": "1",
            "league": "EPL",
            "h": "1.6333",
            "a": "1.3333",
            "hxg": "1.453833992779255",
            "axg": "1.4325587471326193",
            "year": "2018",
            "month": "8",
            "matches": "30"
        }
    ]

---

.. automethod:: understat.Understat.get_team_fixtures

It returns the upcoming fixtures (not results) of the given team, in the given
season. So for example, the fixtures as seen in the screenshot below

.. image:: https://i.imgur.com/0qZbE8a.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. This is similar
to the `get_league_fixtures` function, but it makes certain options for
filtering much easier. For example, if you, once again, wanted to get all
Manchester United's upcoming fixtures at **home**, then instead of passing a
dictionary as keyword argument, you could simply do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            results = await understat.get_team_fixtures(
                "Manchester United",
                2018,
                side="h"
            )
            print(json.dumps(results))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    [
        {
            "id": "9501",
            "isResult": false,
            "side": "h",
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
        ...,
        {
            "id": "9570",
            "isResult": false,
            "side": "h",
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

---

.. automethod:: understat.Understat.get_team_players

It returns all the information about the players of a given team in the given
season. This includes stuff like their number of goals scored, their total
expected assists and more. Basically, it's all the information you can find
in the player table shown on all team overview pages on
`understat.com <https://understat.com>`_.

.. image:: https://i.imgur.com/N53k9Ao.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. This is similar
to the `get_league_players` function, but is quicker and easier. For example,
if you, once again, wanted to get all Manchester United's players who have only
played games as a forward, then you could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            results = await understat.get_team_players(
                "Manchester United",
                2018,
                position="F S"
            )
            print(json.dumps(results))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs

.. code-block:: javascript

    [
        {
            "id": "594",
            "player_name": "Romelu Lukaku",
            "games": "27",
            "time": "1768",
            "goals": "12",
            "xG": "12.054240763187408",
            "assists": "0",
            "xA": "1.6836179178208113",
            "shots": "50",
            "key_passes": "17",
            "yellow_cards": "4",
            "red_cards": "0",
            "position": "F S",
            "team_title": "Manchester United",
            "npg": "12",
            "npxG": "12.054240763187408",
            "xGChain": "12.832402393221855",
            "xGBuildup": "3.366600174456835"
        }
    ]

---

.. automethod:: understat.Understat.get_team_results

It returns the results (not fixtures) of the given team, in the given season.
So for example, the fixtures as seen in the screenshot below

.. image:: https://i.imgur.com/Q9KC5f9.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. This is similar
to the `get_league_results` function, but it makes certain options for
filtering much easier. For example, if you, once again, wanted to get all
Manchester United's results at **home**, then instead of passing a dictionary
as keyword argument, you could simply do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            results = await understat.get_team_results(
                "Manchester United",
                2018,
                side="h"
            )
            print(json.dumps(results))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    [
        {
            "id": "9197",
            "isResult": true,
            "side": "h",
            "h": {
                "id": "89",
                "title": "Manchester United",
                "short_title": "MUN"
            },
            "a": {
                "id": "75",
                "title": "Leicester",
                "short_title": "LEI"
            },
            "goals": {
                "h": "2",
                "a": "1"
            },
            "xG": {
                "h": "1.5137",
                "a": "1.73813"
            },
            "datetime": "2018-08-10 22:00:00",
            "forecast": {
                "w": 0.33715468577027,
                "d": 0.23067469101496,
                "l": 0.43217062251974
            },
            "result": "w"
        },
        ...,
        {
            "id": "9226",
            "isResult": true,
            "side": "h",
            "h": {
                "id": "89",
                "title": "Manchester United",
                "short_title": "MUN"
            },
            "a": {
                "id": "82",
                "title": "Tottenham",
                "short_title": "TOT"
            },
            "goals": {
                "h": "0",
                "a": "3"
            },
            "xG": {
                "h": "1.40321",
                "a": "1.80811"
            },
            "datetime": "2018-08-27 22:00:00",
            "forecast": {
                "w": 0.29970781519619,
                "d": 0.22891929318443,
                "l": 0.47137289056693
            },
            "result": "l"
        }
    ]

---

.. automethod:: understat.Understat.get_team_stats

It returns all the statistics of a given team, which includes stuff like
their performance per season, formation and more. Basically, it's everything
that can be found in the table shown in the screenshot below

.. image:: https://i.imgur.com/RlWzExr.png

An example of getting Manchester United's data can be found below

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            team_stats = await understat.get_team_stats("Manchester United", 2018)
            print(json.dumps(team_stats))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    {
        "situation": {
            "OpenPlay": {
                "shots": 297,
                "goals": 39,
                "xG": 36.671056651045,
                "against": {
                    "shots": 279,
                    "goals": 25,
                    "xG": 28.870285989717
                }
            },
            ...,
            "Penalty": {
                "shots": 10,
                "goals": 7,
                "xG": 7.611688375473,
                "against": {
                    "shots": 5,
                    "goals": 5,
                    "xG": 3.8058441877365
                }
            }
        },
        "formation": {
            "4-3-3": {
                "stat": "4-3-3",
                "time": 1295,
                "shots": 185,
                "goals": 30,
                "xG": 27.7899469533,
                "against": {
                    "shots": 176,
                    "goals": 18,
                    "xG": 20.478145442903
                }
            },
            ...,
            "4-4-2": {
                "stat": "4-4-2",
                "time": 38,
                "shots": 8,
                "goals": 0,
                "xG": 0.87938431277871,
                "against": {
                    "shots": 11,
                    "goals": 1,
                    "xG": 0.66449437476695
                }
            }
        },
        "gameState": {
            "Goal diff 0": {
                "stat": "Goal diff 0",
                "time": 1284,
                "shots": 154,
                "goals": 20,
                "xG": 20.433959940448,
                "against": {
                    "shots": 170,
                    "goals": 15,
                    "xG": 17.543024708517
                }
            },
            ...,
            "Goal diff < -1": {
                "stat": "Goal diff < -1",
                "time": 253,
                "shots": 43,
                "goals": 7,
                "xG": 6.4928285568021,
                "against": {
                    "shots": 21,
                    "goals": 1,
                    "xG": 2.9283153852448
                }
            }
        },
        "timing": {
            "1-15": {
                "stat": "1-15",
                "shots": 51,
                "goals": 6,
                "xG": 7.2566251829267,
                "against": {
                    "shots": 72,
                    "goals": 7,
                    "xG": 8.5656435946003
                }
            },
            ...,
            "76+": {
                "stat": "76+",
                "shots": 70,
                "goals": 12,
                "xG": 10.272770666517,
                "against": {
                    "shots": 77,
                    "goals": 8,
                    "xG": 10.18940022774
                }
            }
        },
        "shotZone": {
            "ownGoals": {
                "stat": "ownGoals",
                "shots": 0,
                "goals": 0,
                "xG": 0,
                "against": {
                    "shots": 2,
                    "goals": 2,
                    "xG": 2
                }
            },
            "shotOboxTotal": {
                "stat": "shotOboxTotal",
                "shots": 158,
                "goals": 8,
                "xG": 4.8084309450351,
                "against": {
                    "shots": 170,
                    "goals": 6,
                    "xG": 5.4022304248065
                }
            },
            ...,
            "shotSixYardBox": {
                "stat": "shotSixYardBox",
                "shots": 36,
                "goals": 13,
                "xG": 13.912872407585,
                "against": {
                    "shots": 32,
                    "goals": 8,
                    "xG": 11.533062046394
                }
            }
        },
        "attackSpeed": {
            "Normal": {
                "stat": "Normal",
                "shots": 258,
                "goals": 34,
                "xG": 30.690259062219,
                "against": {
                    "shots": 230,
                    "goals": 18,
                    "xG": 23.094043077901
                }
            },
            ...,
            "Slow": {
                "stat": "Slow",
                "shots": 18,
                "goals": 2,
                "xG": 0.71848054975271,
                "against": {
                    "shots": 26,
                    "goals": 5,
                    "xG": 2.9855494443327
                }
            }
        },
        "result": {
            "MissedShots": {
                "shots": 122,
                "goals": 0,
                "xG": 12.353983599227,
                "against": {
                    "shots": 155,
                    "goals": 0,
                    "xG": 13.091518453322
                }
            },
            ...,
            "ShotOnPost": {
                "shots": 4,
                "goals": 0,
                "xG": 0.81487018615007,
                "against": {
                    "shots": 2,
                    "goals": 0,
                    "xG": 0.61989105120301
                }
            }
        }
    }

---

.. automethod:: understat.Understat.get_teams

It returns all the information for the teams in a given league, in a given
season. Basically it is all the information that is shown in the league's
table, as shown in the screenshot below

.. image:: https://i.imgur.com/tQO7cnO.png

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output. So for example,
if you wanted to get Manchester United's stats (as shown in the table), you
could do the following

.. code-block:: python

    async def main():
        async with aiohttp.ClientSession() as session:
            understat = Understat(session)
            teams = await understat.get_teams(
                "epl",
                2018,
                title="Manchester United"
            )
            print(json.dumps(teams))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

which outputs (with parts omitted)

.. code-block:: javascript

    [
        {
            "id": "89",
            "title": "Manchester United",
            "history": [
                {
                    "h_a": "h",
                    "xG": 1.5137,
                    "xGA": 1.73813,
                    "npxG": 0.75253,
                    "npxGA": 1.73813,
                    "ppda": {
                    "att": 285,
                    "def": 18
                    },
                    "ppda_allowed": {
                    "att": 298,
                    "def": 26
                    },
                    "deep": 3,
                    "deep_allowed": 10,
                    "scored": 2,
                    "missed": 1,
                    "xpts": 1.1711,
                    "result": "w",
                    "date": "2018-08-10 22:00:00",
                    "wins": 1,
                    "draws": 0,
                    "loses": 0,
                    "pts": 3,
                    "npxGD": -0.9856
                },
                ...,
                {
                    "h_a": "a",
                    "xG": 2.3703,
                    "xGA": 1.52723,
                    "npxG": 2.3703,
                    "npxGA": 0.766059,
                    "ppda": {
                    "att": 203,
                    "def": 25
                    },
                    "ppda_allowed": {
                    "att": 271,
                    "def": 21
                    },
                    "deep": 7,
                    "deep_allowed": 9,
                    "scored": 0,
                    "missed": 2,
                    "xpts": 2.0459,
                    "result": "l",
                    "date": "2019-03-10 16:30:00",
                    "wins": 0,
                    "draws": 0,
                    "loses": 1,
                    "pts": 0,
                    "npxGD": 1.604241
                }
            ]
        }
    ]
