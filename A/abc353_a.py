def run():
    N = int(input())
    H_array = list(map(int, input().split(" ")))
    top = -1

    for i in range(N):
        if i == 0:
            continue
        first = H_array[0]
        if H_array[i] > first:
            top = i + 1
            break

    print(top)


if __name__ == '__main__':
    run()
