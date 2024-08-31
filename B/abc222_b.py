def run():
    N, P = map(int, input().split(" "))
    a_array = list(map(int, input().split(" ")))
    result = 0
    for i in range(N):
        if a_array[i] < P:
            result += 1

    print(result)


if __name__ == '__main__':
    run()
