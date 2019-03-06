import aiohttp
import pytest

from understat import Understat


@pytest.fixture()
async def understat():
    session = aiohttp.ClientSession()
    fpl = Understat(session)
    yield fpl
    await session.close()
