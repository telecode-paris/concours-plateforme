#
# 100% inspiré du problème F de la SWERC 2019.
# https://swerc.eu/2019/theme/problems/swerc.pdf
#

# simplement la formule https://fr.wikipedia.org/wiki/Aire_d%27un_polygone
# attention renvoie l'aire négative si les points sont dans l'ordre horaire (positif si trigo)
def area(l):
    s = 0
    for i, (x, y) in enumerate(l):
        xx, yy = l[0] if i == len(l) - 1 else l[i + 1]
        s += x * yy - y * xx
    return s

def polygons():
    N = int(input())
    s = 0

    for _ in range(N):
        l = []
        P = int(input())
        for _ in range(P):
            x, y = map(int, input().split())
            l.append((x, y))
        s += abs(area(l))

    print(int(s / 2))

if __name__ == "__main__":
    polygons()
