import random
import run_test
import RainbowRider.solve

NAME_RAINBOW = "Arcs-en-ciel"

def generate_line(N):
    MAX = 10**9
    D = random.randint(2, MAX)
    print(N, D)
    seen = set()
    seen.add(1)
    seen.add(D)
    prev = 1
    for _ in range(1, N):
        while True:
            cur = random.randint(2, MAX)
            if cur not in seen:
                print(prev, cur)
                seen.add(cur)
                prev = cur
                break
    print(prev, D)

def generate(max_n, num_vertex, num_edges):
    MAX = 10**9
    vertices = set()
    for _ in range(2, num_vertex):
        while True:
            e = random.randint(2, MAX)
            if e not in vertices:
                vertices.add(e)
                break

    D = random.randint(2, max_n)

    vertices.add(1)
    vertices.add(D)
    vertices = list(vertices)

    edges = {}
    for e in vertices:
        edges[e] = set()

    for _ in range(num_edges):
        while True:
            a = random.choice(vertices)
            b = random.choice(vertices)
            if a == b:
                continue
            if b not in edges[a]:
                edges[a].add(b)
                edges[b].add(a)
                break

    print(num_edges, D)
    for a, e in edges.items():
        for b in e:
            if a > b:
                print(a, b)

def gen():
    fp = RainbowRider.solve.rainbow

    li = []

    inputs = ["3 2\n4 3\n1 5\n3 5\n", "3 4\n1 2\n2 3\n3 4\n", "3 1\n2 3\n1 5\n7 2\n"]

    for i in range(1, 8):
        with open("RainbowRider/test{}.in".format(i)) as f:
            inputs.append(f.read())

    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("RainbowRider/page.html") as f:
        description = f.read()

    return (NAME_RAINBOW, description, 0, li)
