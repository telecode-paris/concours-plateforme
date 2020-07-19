import math

def convex_hull():
    def distance(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    def andrew_monotone_chain(points):
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        points = sorted(set(points))
        length = len(points)

        if length < 3:
            return points

        upper = []
        lower = []

        for i in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], i) <= 0:
                lower.pop()
            lower.append(i)

        for i in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], i) <= 0:
                upper.pop()
            upper.append(i)

        return lower[:-1] + upper[:-1]

    N = int(input())
    points = []

    for i in range(N):
        (a, b) = input().split()
        (a, b) = (float(a), float(b))
        points.append((a, b))

    hull = andrew_monotone_chain(points)

    perimetre = 0
    length = len(hull)
    if length == 1:
        return 0
    elif length == 2:
        return math.ceil(distance(hull[0], hull[1]))
    else:
        for i in range(length):
            perimetre += distance(hull[i], hull[(i + 1) % length])

    print(math.ceil(perimetre))

if __name__ == "__main__":
    convex_hull()
