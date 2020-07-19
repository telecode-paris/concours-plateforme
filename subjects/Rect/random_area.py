from random import random
from Rect.solve import rect

def random_area(height, width, block_proportion = 0.1) :
    out = []
    for i in range(height):
        s = ""
        for j in range(width):
            if random() < block_proportion:
                s += "*"
            else:
                s += "."
        out.append(s)

    c = rect((height, width, out), True)

    if len(c) > 1:
        for i in range(len(c) - 1):
            l = list(out[c[i][0]])
            l[c[i][1]] = "*"
            out[c[i][0]] = "".join(l)

    out_bis = str(height) + " " + str(width) + "\n"
    for i in out:
        out_bis += i + "\n"
    
    return out_bis

if __name__ == '__main__':
    (a, b) = [int(i) for i in input().split()]
    a = random_area(a, b, random()/5 + 0.1)
    print(a)
