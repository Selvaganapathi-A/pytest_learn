from app.package_02.script_13 import add, multiply

import pytest


@pytest.mark.asyncio
async def test__add():
    assert await add(987, 64) == 1051


@pytest.mark.asyncio
async def test__multiply():
    assert await multiply(7, 9) == 63
