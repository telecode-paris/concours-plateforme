import run_test
import Palindrome.solve

NAME_PALINDROME = "Palindrome"

def gen():
    fp = Palindrome.solve.palindrom

    li = []

    inputs = ["A Santa dog lived as a devil God at NASA",\
        "A nut for a jar of tuna",\
        "Multi tasking a future", \
        "Im going alula here", \
        "aaffaabbaaffaaggaaffaabb", \
        "A late metal has a level Multi tasking a future Lag not Eno No gong Get up Put eggnog on one-ton gal A nut for a jar of tuna", \
        "Live evil is better than alula", \
        "nop", \
        "Raising hell on eart for lion oil in a zoo", \
        "in the aaaaooaaaa what"]

    for st in inputs:
        s = st.lower()
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("Palindrome/page.html") as f:
        description = f.read()

    return (NAME_PALINDROME, description, 0, li)
