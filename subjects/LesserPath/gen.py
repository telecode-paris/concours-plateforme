import random
import run_test
import LesserPath.solve

NAME_LESSER = "Malédiction"

def generator(N, M):
    print(N, M)

    D = random.randint(0, N - 1)
    A = D
    while A == D:
        A = random.randint(0, N - 1)

    print(D, A)

    edges = [{} for _ in range(N)]

    for _ in range(M):
        while True:
            u = random.randint(0, N - 1)
            v = random.randint(0, N - 1)
            if u != v and v not in edges[u]:
                p = random.randint(1, 10**3)
                edges[u][v] = p
                print(u, v, p)
                break

def gen():
    fp = LesserPath.solve.lesser

    li = []

    inputs = ["7 9\n0 6\n0 1 1\n0 2 1\n0 3 2\n0 4 3\n1 5 2\n2 6 4\n3 6 2\n4 6 4\n5 6 1\n", "4 6\n0 2\n0 1 1\n1 2 1\n1 3 1\n3 2 1\n2 0 3\n3 0 2\n"]

    for i in range(0, 9):
        with open("LesserPath/test{}".format(i)) as f:
            inputs.append(f.read())

    i = 0
    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 10+i))
        i+=1

    description = ""
    with open("LesserPath/page.html") as f:
        description = f.read()

    return (NAME_LESSER, description, 2, li)
