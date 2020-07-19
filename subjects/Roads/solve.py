from collections import deque

def roads():
    N = int(input())
    values = [0 for _ in range(N - 1)]
    edges = []
    neighbors = [[] for _ in range(N)]
    weights = []

    for i in range(N - 1):
        a, b, l = map(int, input().split())
        a -= 1
        b -= 1
        edges.append((a, b))
        neighbors[a].append((i, b))
        neighbors[b].append((i, a))
        weights.append(l)

    stack = []
    fifo = deque([(0, edges[0][0]), (0, edges[0][1])])

    while fifo:
        prev_edge, elem = fifo.pop()
        stack.append((prev_edge, elem))
        for edge in neighbors[elem]:
            if edge[0] != prev_edge:
                fifo.append(edge)

    while stack:
        prev_edge, elem = stack.pop()
        values[prev_edge] = 1
        for edge in neighbors[elem]:
            if edge[0] != prev_edge:
                values[prev_edge] += values[edge[0]]


    sum_of_dists = 0
    for i in range(N - 1):
        l = values[i]
        # print("{}: {}".format(i + 1, l))
        sum_of_dists += l * (N - l) * weights[i]

    print("{0:.6f}".format(sum_of_dists * 2 / (N * (N - 1))))
    Q = int(input())
    for i in range(Q):
        r, w = map(int, input().split())
        r -= 1
        l = values[r]
        sum_of_dists += l * (N - l) * (w - weights[r])
        weights[r] = w
        print("{0:.6f}".format(sum_of_dists * 2 / (N * (N - 1))))

if __name__ == "__main__":
    roads()
