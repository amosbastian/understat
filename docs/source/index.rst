A Python wrapper for the Fantasy Premier League API
===================================================

.. image:: https://api.codacy.com/project/badge/Grade/716b2c24086a41d7a79481ac89748861
    :target: https://www.codacy.com/app/amosbastian/understat?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=amosbastian/understat&amp;utm_campaign=Badge_Grade

.. image:: https://travis-ci.com/amosbastian/understat.svg?branch=master
    :target: https://travis-ci.com/amosbastian/understat

.. image:: https://img.shields.io/badge/Supported%20by-Utopian.io-%23B10DC9.svg
    :target: https://utopian.io/

.. image:: https://badge.fury.io/py/understat.svg
    :target: https://pypi.org/project/understat/

.. image:: https://img.shields.io/badge/Python-3.6%2B-blue.svg
    :target: https://pypi.org/project/understat/


.. note:: The latest version of **understat** is asynchronous, and requires Python 3.6+!

If you're interested in helping out the development of **understat**, or have
suggestions and ideas then please don't hesitate to create an issue on GitHub,
join our `Discord server <https://discord.gg/cjY37fv>`_ or send an email to
`amosbastian@gmail.com <mailto:amosbastian@gmail.com>`_!

--------------

**A simple example**::

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


With **understat** you can easily get all the data available on `understat.com
<https://understat.com/>`_!

The User Guide
--------------

This part of the documentation simply shows you have to install **understat**.

.. toctree::
   :maxdepth: 2

   user/installation

The Class Documentation / Guide
-------------------------------

This part of the documentation is for people who want or need more information
bout specific functions and classes found in **understat**. It includes example
output for each of the functions, and also screenshots showing where you would
find the equivalent data on `understat.com <https://understat.com>`_.

.. toctree::
   :maxdepth: 2

   classes/understat


The Contributor Guide
---------------------

If you want to help **understat** out and contribute to the project, be it via
development, suggestions, hunting bugs etc. then this part of the documentation
is for you!

.. toctree::
   :maxdepth: 2

   contributing/contributing
   contributing/authors