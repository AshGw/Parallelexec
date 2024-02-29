import random
import time
from parallelexec import ParallelExec

_RUNS: int = 10


def one():
    for _ in range(_RUNS):
        print(54 + 64 * random.randint(1, 10))
        time.sleep(0.5)


def two():
    for _ in range(_RUNS):
        print(54 - 64 * random.randint(1, 10))
        time.sleep(0.5)


def three():
    for _ in range(_RUNS):
        print(0)
        time.sleep(0.5)


if __name__ == "__main__":

    @ParallelExec.processor([one, two, three], join=True)
    def run():
        ...

    print("This will run anyway")

    run()

    print("if join is True this should only show up if run() has finished executing")
    print("same here")
