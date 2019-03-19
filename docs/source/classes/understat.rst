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

The function comes with the `options` keyword argument, and the `**kwargs`
magic variable, and so that can be used to filter the output.
So for example, if you wanted to get all Manchester United's upcoming fixtures,
then you could do the following

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

.. image:: https://i.imgur.com/dE54ox0.png

This function, as many other functions, also comes with the `options` keyword
argument, and also the `**kwargs` magic variable. An example of how you could
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
variable have been shown, the examples will only use *one* of these from now on.

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

---

.. automethod:: understat.Understat.get_players

---

.. automethod:: understat.Understat.get_results

---

.. image:: https://i.imgur.com/5rf0ACo.png

.. automethod:: understat.Understat.get_stats

---

.. automethod:: understat.Understat.get_team_stats

---

.. automethod:: understat.Understat.get_teams

