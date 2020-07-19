
# simplement un tri baquet pour trouver la médiane
def mediane():
    N = int(input())
    numbers = [0 for _ in range(10001)]
    for _ in range(N):
        numbers[int(input())] += 1

    acc = 0
    for i, e in enumerate(numbers):
        acc += e

        if acc > N / 2:
            print(i)
            return

if __name__ == "__main__":
    mediane()
