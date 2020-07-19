import run_test
import Hello.solve

NAME_HELLO = "Hello"

def gen():
    fp = Hello.solve.hello

    li = []

    inputs = ["ip7", "Einstein", "Tobi", "World"]

    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("Hello/page.html") as f:
        description = f.read()

    return (NAME_HELLO, description, 0, li)
