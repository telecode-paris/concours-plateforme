def cycle():
    A, B, C, D, M = map(int, input().split())
    MOD = 2 ** M

    def f(x):
        return (A * x + B + (x >> C) + (x << D)) % MOD

    prev = 1
    cur = 1
    ens = 0
    while not ens & (1 << cur):
        ens |= 1 << cur
        prev, cur = cur, f(cur)

    print(prev)

# pour afficher tous les éléments d'une suite
def calc(A, B, C, D, M):
    x0 = 1
    print(x0, end=' ')
    for _ in range(2**M):
        x0 = (A * x0 + B + (x0 >> C) + (x0 << D)) % (2 ** M)
        print(x0, end=' ')
    print()

if __name__ == "__main__":
    cycle()
