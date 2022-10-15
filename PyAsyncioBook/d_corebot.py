import asyncio
import sys

from attr import attrib, attrs


@attrs
class Cutlery:
    knives: int = attrib(default=0)
    forks: int = attrib(default=0)

    def give(self, to: "Cutlery", knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


class CoroBot:
    def __init__(self):
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = asyncio.Queue()

    async def manage_table(self):
        while True:
            task = await self.tasks.get()
            if task == "prepare table":
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == "clear table":
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == "shutdown":
                return
            else:
                raise Exception("Unsupported task")


kitchen = Cutlery(knives=100, forks=100)

for bot in (bots := [CoroBot() for _ in range(10)]):
    for i in range(int(sys.argv[1])):
        bot.tasks.put_nowait("prepare table")
        bot.tasks.put_nowait("clear table")
    bot.tasks.put_nowait("shutdown")

print(f"Kitchen inventory before service: {kitchen}")


async def main():
    tasks = []
    for bot in bots:
        task = asyncio.create_task(bot.manage_table())
        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(main())
print(f"Kitchen inventory after service: {kitchen}")
