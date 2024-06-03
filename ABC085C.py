import itertools
def run():
    N, Y = map(int, input().split(" "))
    # N, Y = map(int, "1000 1234000".split(" "))
    # N, Y = map(int, "2000 195400000".split(" "))
    A = 10000
    B = 5000
    C = 1000

    for i in range(0, N + 1):
        for j in range(0, N + 1):
            if N < (i + j):
                continue

            iA = i * A
            jB = j * B
            diff = (N - i - j)
            kC = diff * C
            if(diff < 0):
                diff = 0

            if (iA + jB + kC) == Y:
                return f"{i} {j} {diff}"
            # for k in range(1, N + 1):
            #     if total == Y:
            #         print(total, Y)
            #         return f"{i} {j} {k}"

    return "-1 -1 -1"

if __name__ == '__main__':
    res = run()
    print(res)
