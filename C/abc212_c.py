import bisect


def run():
    # N, M = map(int, "6 8".split(" "))
    # A = list(map(int, "25 76 1 82 71 70".split(" ")))
    # B = list(map(int, "2 17 22 24 35 39 45 67".split(" ")))
    N, M = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    B.sort()
    # print(B)
    result = float("inf")

    for i in range(N):
        pos = bisect.bisect_left(B, A[i])
        # print(f"pos={pos}")
        if pos == M:
            result = min(result, abs(B[M - 1] - A[i]))
            # print("a", result, f"A={A[i]},B={B[pos - 1]}")
        elif pos == 0:
            result = min(result, abs(B[0] - A[i]))
            # print("b", result, f"A={A[i]},B={B[pos]}")
        else:
            result = min(result, abs(B[pos] - A[i]), abs(B[pos - 1] - A[i]))
            # print("c", result, f"A={A[i]},B={B[pos]}")

    print(result)


if __name__ == '__main__':
    run()
