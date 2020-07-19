import run_test
import Convex_Hull.solve
import Convex_Hull.random_dist
from random import randint

NAME_CONVEX_HULL = "Murailles"

def gen():
    fp = Convex_Hull.solve.convex_hull

    li = []

    inputs = []
    for i in range(10):
        po = 2 ** (i + 2)
        b_max = po + 10
        b_min = i*2 + 5
        inputs.append(Convex_Hull.random_dist.random_points_distribution(n = po + b_min ** 2, x_min = randint(-b_max, -(b_min)), x_max = randint(b_min, b_max), y_min = randint(-(b_max), -(b_min)), y_max = randint(b_min, b_max)))

    inputs_bis = []
    for i in inputs:
        s = str(len(i)) + "\n"
        for p in i:
            s_bis = str(p[0]) + " " + str(p[1]) + "\n"
            s += s_bis
        inputs_bis.append(s)

    i = 0
    for st in inputs_bis:
        li.append((st, run_test.get_res_test(st, fp), 1, 5 + (i / 2)))
        i+=1

    description = ""
    with open("Convex_Hull/page.html") as f:
        description = f.read()

    return (NAME_CONVEX_HULL, description, 1, li)
