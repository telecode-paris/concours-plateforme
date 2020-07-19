from random import randint

def random_points_distribution(n = 10, x_min = 0, x_max = 10, y_min = 0, y_max = 10):
    l = []
    while len(l) < n:
        for i in range(n - len(l)):
            p = (randint(x_min, x_max), randint(y_min, y_max))
            l.append(p)
        l = list(set(l))
    return l


if __name__ == "__main__":
    n, x_min, x_max, y_min, y_max = [int(a) for a in input().split()]
    points = random_points_distribution(n, x_min, x_max, y_min, y_max)
    s = str(len(points)) + "\n"
    for p in points:
        s_bis = str(p[0]) + " " + str(p[1]) + "\n"
        s += s_bis
    print (s)
    
    
    # inputs = []
    # for i in range(10):
    #     po = 2 ** (i + 2)
    #     b_max = po + 10
    #     b_min = i*2 + 5
    #     inputs.append(random_points_distribution(n = po + b_min ** 2, x_min = randint(-b_max, -(b_min)), x_max = randint(b_min, b_max), y_min = randint(-(b_max), -(b_min)), y_max = randint(b_min, b_max)))
    
    # inputs_bis = []
    # for i in inputs:
    #     s = str(len(i)) + "\n"
    #     for p in i:
    #         s_bis = str(p[0]) + " " + str(p[1]) + "\n"
    #         s += s_bis
    #     inputs_bis.append(s)
    # for i in inputs_bis:
    #     print(i)