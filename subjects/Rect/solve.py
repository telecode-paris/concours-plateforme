import math
import collections
from random import random

def print_2D(l):
    for i in l:
        print(i)

def count(size, val):
    count = []
    for i in range(len(size)):
        for j in range(len(size[0])):
            if size[i][j] == val:
                count.append((i, j))
    return count

def rect_from_input():
    lst = input().split()
    (H, W) = (int(lst[0]), int(lst[1]))

    lines = []

    for i in range(H):
        lines.append(input())

    return rect((H, W, lines))

def rect(solve_from, output_count = False):
    def free_column(h, w, l, area, size):
        for i in range(l + 1):
            if not area[h + i][w]:
                return False
        return True

    def free_line(h, w, l, area, size):#
        for i in range(l + 1):
            if not area[h][w + i]:
                return False
        return True

    def update(h, w, s, size):
        for i in range(s):
            for j in range(s):
                t = min(s - i, s - j)
                if size[h + i][w + j] < t:
                    size[h + i][w + j] = t

    def square(h, w, area, size):
        if not area[h][w]:
            return 0
        for i in range (size[h][w], len(area) - h):
            if not (free_line(h + i, w, i, area, size) and free_column(h, w + i, i, area, size)):
                return i
        return i


    to_bool = lambda x : x == "."

    (H, W, lines) = solve_from

    area = []
    size = []

    for l in lines:
        a = []
        for i in l:
            a.append(to_bool(i))
        area.append(a + [False])
        size.append([0] * (W))
    area.append([False] * (W + 1))

    c = (0, 0)
    for i in range(H):
        for j in range(W):
            if H - i - size[c[0]][c[1]] < 0 or W - j - size[c[0]][c[1]] < 0 :
                break
            s = square(i, j, area, size)
            update(i, j, s, size)
            if size[c[0]][c[1]] < s:
                c = (i, j)

    if output_count:
        return count(size, size[c[0]][c[1]])
    print (str(c[0]) + " " + str(c[1]))
    return str(c[0]) + " " + str(c[1])

if __name__ == '__main__':
    print(rect_from_input())
