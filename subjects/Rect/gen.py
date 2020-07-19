import run_test
import Rect.solve
from random import random
from random import randint
from Rect.random_area import random_area
import Rect.solve

NAME_RECT = "Rect"


def gen():

    fp = Rect.solve.rect_from_input

    li = []

    inputs = []
    for i in range(10):
        po = 2 ** (i + 1)
        inputs.append(random_area(po, randint(po//2, po), random()/5 + 0.1))

    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("Rect/page.html") as f:
        description = f.read()

    return (NAME_RECT, description, 0, li)
