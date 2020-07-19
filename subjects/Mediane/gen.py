from random import randint
import run_test
import Mediane.solve

NAME_MEDIANE = "Fleurs"

MAX_N = 10000000
MAX_NOTE = 10000
MIN_NOTE = 1

def create(N):
    acc = "{}\n".format(N)

    while N > 0:
        N -= 1
        acc += str(randint(MIN_NOTE, MAX_NOTE)) + '\n'

    return acc

def gen():
    fp = Mediane.solve.mediane

    inputs = [create(10), create(10), create(10), create(50), create(50), create(100), create(100), create(10000), create(10000), create(100000)]

    li = []

    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("Mediane/page.html") as f:
        description = f.read()

    return (NAME_MEDIANE, description, 0, li)
