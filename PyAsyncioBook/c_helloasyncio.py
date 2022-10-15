import asyncio
import time
from typing import Any, Coroutine


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1)
    print(f"{time.ctime()} Goodbye!")


def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")


# asyncio.run(main())


def get_or_create_eventloop() -> asyncio.AbstractEventLoop:
    try:
        return asyncio.get_event_loop()
    except DeprecationWarning:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return asyncio.get_event_loop()


def asyncio_run(func: Coroutine[Any, Any, None]):
    loop = get_or_create_eventloop()
    task = loop.create_task(func)

    loop.run_in_executor(None, blocking)
    loop.run_until_complete(task)

    for task in (pending := asyncio.all_tasks(loop=loop)):
        task.cancel()

    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()

asyncio_run(main())
