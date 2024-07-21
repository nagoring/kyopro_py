import math


def run():
    N = int(input())
    for k in range(60):
        if N < 2 ** (k + 1):
            print(k)
            return

    # res = math.log2(int(input()))
    # print(math.floor(res))


if __name__ == '__main__':
    run()
