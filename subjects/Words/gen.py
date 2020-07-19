import random

import run_test
import Words.solve

NAME_WORDS = "Mots"

# generate a list of words with one element who appears more than the others
def gen_text(words):
    s = []
    lenw = len(words)

    occ = [0] * (len(words))
    while (len(s) * 20 < 10000):
        w = random.randrange(0,lenw)
        occ[w] += 1
        s.append(words[w])

    m = max(occ)
    if (occ.count(m) > 1):
        s.append(words[occ.index(m)])
    return s

def gen():
    fp = Words.solve.words

    li = []

    words = ["krakus", "alar", "tobi", "azimov", "arkane", "tolkien", "lovecraft", "valar",
              "morgoth", "erlie", "zappatta", "mozart", "zimbabwe", "epiphanie", "youpi",
              "erzok", "martin", "antigone"]

    inputs = []

    for i in range(0,10):
        inputs.append(' '.join(gen_text(words)))

    for st in inputs:
        li.append((st, run_test.get_res_test(st, fp), 1, 1))

    description = ""
    with open("Words/page.html") as f:
        description = f.read()

    return (NAME_WORDS, description, 0, li)
