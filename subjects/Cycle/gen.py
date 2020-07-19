import random
import run_test
import Cycle.solve

# inspiré de manière très très lointaine de l'exercice H de la SWERC 2019
# https://swerc.eu/2019/theme/problems/swerc.pdf#page=19
NAME_CYCLE = "Cycle"

def generate(max_M):
    M = random.randint(1, max_M)
    A = random.randint(0, 2**M - 1)
    B = random.randint(0, 2**M - 1)
    C = random.randint(0, M)
    D = random.randint(0, M)
    return "{} {} {} {} {}\n".format(A, B, C, D, M)

def gen():
    fp = Cycle.solve.cycle

    li = []

    inputs = ["1 1 1 1 3\n", "1 2 3 2 4\n", "1165 2569 13 3 13\n", "13812 12642 10 2 14\n", "20057 21554 15 8 15\n", "7265 46726 16 6 16\n", "30545 112741 3 16 18\n", "238767 45165 4 4 19\n", "95483 320692 13 18 20\n", "499452 440880 11 5 20\n", "198098 2074428 3 2 21\n", "13 2 5 7 22\n"]

    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("Cycle/page.html") as f:
        description = f.read()

    return (NAME_CYCLE, description, 0, li)
