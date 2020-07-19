import random
import run_test
import Roads.solve

# inspiré de https://codeforces.com/problemset/problem/500/D
NAME_ROADS = "Routes"

MAX_N = 100000
MAX_Q = 1000
MAX_W = 10000

def gen_input(N, Q):
    acc = ""

    acc += "{}\n".format(N)
    vals = []
    for count in range(1, N):
        vals.append(random.randrange(MAX_W))
        acc += "{} {} {}\n".format(count + 1, random.randrange(count) + 1, vals[-1])

    acc += "{}\n".format(Q)
    while Q > 0:
        ind = random.randrange(N - 1)
        vals[ind] = random.randrange(MAX_W)
        acc += "{} {}\n".format(ind + 1, vals[ind])
        Q -= 1

    return acc

small_example = "3\n1 2 5\n3 1 4\n2\n1 3\n1 1\n"

# l'arbre est ici une suite d'arêtes, utile pour faire planter les algos récursifs
def gen_line(N, Q):
    acc = ""

    acc += "{}\n".format(N)
    vals = []
    for count in range(1, N):
        vals.append(random.randrange(MAX_W))
        acc += "{} {} {}\n".format(count + 1, count, vals[-1])

    acc += "{}\n".format(Q)
    while Q > 0:
        ind = random.randrange(N - 1)
        vals[ind] = random.randrange(MAX_W)
        acc += "{} {}\n".format(ind + 1, vals[ind])
        Q -= 1

    return acc

def gen():
    fp = Roads.solve.roads

    li = []

    inputs = [small_example]
    for _ in range(5):
        inputs.append(gen_input(1000, 100))
    for _ in range(5):
        inputs.append(gen_input(MAX_N, MAX_Q))
    inputs.append(gen_line(MAX_N, MAX_Q))

    i=0
    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 10 + i))
        i+=1

    description = ""
    with open("Roads/page.html") as f:
        description = f.read()

    return (NAME_ROADS, description, 2, li)
