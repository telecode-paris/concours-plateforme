import sys
from heapq import heappush, heappop

def lesser():
    N, M = map(int, input().split())
    S, D = map(int, input().split())

    edges = [{} for _ in range(N)]
    for i in range(M):
        u, v, p = map(int, input().split())
        edges[u][v] = p

    previous = [[] for _ in range(N)]
    distances = [-1 for _ in range(N)]
    distances[S] = 0

    queue = []
    heappush(queue, (0, S))

    while queue:
        d, e = heappop(queue)

        if distances[D] != -1 and d > distances[D]:
            break
        if d != distances[e]:
            continue

        for edge in edges[e].items():
            v, p = edge
            if distances[v] == -1 or d + p <= distances[v]:
                if distances[v] == -1 or d + p < distances[v]:
                    distances[v] = d + p
                    previous[v].clear()
                previous[v].append(e)
                heappush(queue, (d + p, v))

    for i, e in enumerate(distances):
        if i == D:
            print(i, e, "END", file=sys.stderr)
        else:
            print(i, e, file=sys.stderr)

    remove = []
    for prev in previous[D]:
        remove.append((prev, D))
    previous[D].clear()

    while remove:
        u, v = remove.pop()
        print(u, "==>", v, file=sys.stderr)

        for prev in previous[u]:
            remove.append((prev, u))
        previous[u].clear()

        edges[u].pop(v, 0)

    queue = []
    heappush(queue, (0, S))

    for i in range(N):
        distances[i] = -1
    distances[S] = 0

    while queue:
        d, u = heappop(queue)

        if u == D:
            break

        if d != distances[u]:
            continue

        for edge in edges[u].items():
            v, p = edge
            if distances[v] == -1 or d + p < distances[v]:
                distances[v] = d + p
                heappush(queue, (d + p, v))

    print(distances[D])

if __name__ == "__main__":
    lesser()
