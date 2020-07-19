from collections import deque

def rainbow():
    N, D = map(int, input().split())

    if D == 1:
        print(0)
        return

    edges = {}
    for _ in range(N):
        A, B = map(int, input().split())

        if A in edges:
            edges[A].append(B)
        else:
            edges[A] = [B]

        if B in edges:
            edges[B].append(A)
        else:
            edges[B] = [A]

    if D not in edges or 1 not in edges:
        print("NOPE")
        return

    seen = set()
    seen.add(1)

    q = deque()
    q.append((1, 0))

    while q:
        e, d = q.popleft()
        d += 1
        for o in edges[e]:
            if o not in seen:
                if o == D:
                    print(d)
                    return
                q.append((o, d))
                seen.add(o)

    print("NOPE")

if __name__ == "__main__":
    rainbow()
