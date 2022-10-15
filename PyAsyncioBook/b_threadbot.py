import sys
import threading
from queue import Queue

from attr import attrib, attrs


# This decorator will ensure that the class will get all the
# usual boilerplate code (__init__, etc)
@attrs
class Cutlery:
    knives: int = attrib(default=0)
    forks: int = attrib(default=0)
    lock = threading.Lock()

    def give(self, to: "Cutlery", knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        with self.lock:
            self.knives += knives
            self.forks += forks


class ThreadBot(threading.Thread):
    def __init__(self):
        super().__init__(target=self.manage_table)
        # Each bot keeps track of the cutlery that it took
        # from the kitchen here
        self.cutlery = Cutlery(knives=0, forks=0)
        self.tasks = Queue()

    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == "prepare table":
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == "clear table":
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            elif task == "shutdown":
                return


kitchen = Cutlery(knives=100, forks=100)
bots = [ThreadBot() for _ in range(10)]

for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put("prepare table")
        bot.tasks.put("clear table")
    bot.tasks.put("shutdown")

print("Kitchen inventory before service:", kitchen)
_ = [bot.start() for bot in bots]
_ = [bot.join() for bot in bots]

print("Kitchen inventory after service:", kitchen)
