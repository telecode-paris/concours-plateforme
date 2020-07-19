import run_test
import Hopcroft_Karp.solve
from random import randint

NAME_HOPCROFT_KARP = "Saint-Valentin"

def gen_bipartite_graph(n, max_u, max_y):
    l = []
    while len(l) < n:
        l.append((randint(0, max_u - 1), randint(max_u, max_u + max_y - 1)))
        l = list(set(l))
    return l

def gen():

    fp = Hopcroft_Karp.solve.hopcroft

    li = []

    inputs = []
    for i in range(10):
        po = 2 ** (i + 2)
        inputs.append(gen_bipartite_graph(po, po//2, po//2))

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
    with open("Hopcroft_Karp/page.html") as f:
        description = f.read()

    return (NAME_HOPCROFT_KARP, description, 1, li)
