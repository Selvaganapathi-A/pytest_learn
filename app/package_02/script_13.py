import asyncio


async def add(a: int, b: int):
    await asyncio.sleep(2.5)
    return a + b


async def multiply(a: int, b: int):
    await asyncio.sleep(1.5)
    return a * b
