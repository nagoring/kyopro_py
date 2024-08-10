def run():
    N = int(input())
    A, B = input().split(" ")
    # res = (1 * 2 ** 3) + (0 * 2 ** 2) + (1 * 2 ** 1) + (1 * 2 ** 0)

    index = len(A) - 1
    a_total = 0
    for a in A:
        a_total += int(a) * N ** index
        index -= 1

    index = len(B) - 1
    b_total = 0
    for b in B:
        b_total += int(b) * N ** index
        index -= 1

    res = a_total * b_total
    print(res)


if __name__ == '__main__':
    run()
