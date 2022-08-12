<p align="center">
    A Python package for https://understat.com/.
    <br>
    <br>
    <a href="https://travis-ci.com/amosbastian/understat"><img src="https://travis-ci.com/amosbastian/understat.svg?branch=master"></a>
    <a href="https://pypi.org/project/understat/" alt="Version">
        <img src="https://badge.fury.io/py/understat.svg"/></a>
    <a href="https://pypi.org/project/understat/" alt="Python version">
        <img src="https://img.shields.io/badge/Python-3.6%2B-blue.svg"/></a>
    <a href="https://understat.readthedocs.io/en/latest/" alt="Documentation">
        <img src="https://readthedocs.org/projects/understat/badge/?version=latest&style=flat"></a>
</p>

Join the [Discord server](https://discord.gg/cjY37fv) or submit [an issue](https://github.com/amosbastian/understat/issues) for help and / or suggestions!

## Installing understat

The recommended way to install understat is via `pip`.

    pip install understat

To install it directly from GitHub you can do the following:

    git clone git://github.com/amosbastian/understat.git

You can also install a [.tar file](https://github.com/requests/requests/tarball/master)
or [.zip file](https://github.com/requests/requests/tarball/master)

    curl -OL https://github.com/amosbastian/understat/tarball/master
    curl -OL https://github.com/amosbastian/understat/zipball/master # Windows

Once it has been downloaded you can easily install it using `pip`:

    cd understat
    pip install .

## Usage

An example of using `understat` can be found below:

```python
import asyncio
import json

import aiohttp

from understat import Understat


async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        data = await understat.get_league_players("epl", 2018, {"team_title": "Manchester United"})
        print(json.dumps(data))


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
```


## Contributing

1. Fork the repository on GitHub.
2. Run the tests with `pytest tests/` to confirm they all pass on your system.
   If the tests fail, then try and find out why this is happening. If you aren't
   able to do this yourself, then don't hesitate to either create an issue on
   GitHub, or send an email to [amosbastian@gmail.com](mailto:amosbastian@gmail.com>).
3. Either create your feature and then write tests for it, or do this the other
   way around.
4. Run all tests again with with `pytest tests/` to confirm that everything
   still passes, including your newly added test(s).
5. Create a pull request for the main repository's `master` branch.

## Documentation

Documentation and examples for **understat** can be found at http://understat.readthedocs.io/en/latest/.
