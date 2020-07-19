import run_test
import Polygons.solve

NAME_POLYGON = "Mosaïque"

NUMBER_OF_TESTS = 13

def gen():
    fp = Polygons.solve.polygons

    li = []

    inputs = []
    # inputs stolen from the SWERC problem
    for i in range(1, NUMBER_OF_TESTS + 1):
        with open("Polygons/test{}.in".format(i)) as f:
            inputs.append(f.read())

    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("Polygons/page.html") as f:
        description = f.read()

    return (NAME_POLYGON, description, 0, li)
