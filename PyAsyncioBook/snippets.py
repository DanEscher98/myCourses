import asyncio
from asyncio import StreamReader, StreamWriter


async def doubler(n):
    for i in range(n):
        yield i, i * 2
        await asyncio.sleep(0.1)


async def main_a():
    result = [x async for x in doubler(3)]
    print(result)
    result = {x: y async for x, y in doubler(3)}
    print(result)
    result = {x async for x in doubler(3)}
    print(result)


async def func(x):
    await asyncio.sleep(0.1)
    return x + 100


async def factory(n):
    for x in range(n):
        await asyncio.sleep(0.1)
        yield func, x


async def main_b():
    results = [await f(x) async for f, x in factory(3)]
    print("results", results)


async def echo(reader: StreamReader, writer: StreamWriter):
    print("New connection")
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print("Leaving connection")
    except asyncio.CancelledError:
        print("Connection dropped!")


async def main_c(host="127.0.0.1", port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(main_c())
except KeyboardInterrupt:
    print("Bye!")

asyncio.run(main_a())
asyncio.run(main_b())
