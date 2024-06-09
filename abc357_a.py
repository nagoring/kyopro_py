def run():
    # N, M = map(int, "1 1".split(" "))
    # H_array = list(map(int, "10".split(" ")))
    N, M = map(int, input().split(" "))
    H_array = list(map(int, input().split(" ")))
    res = 0
    output = 0
    for i in range(N):
        value = H_array[i]
        res += value
        if M < res:
            output = i
            break
        output = i + 1

    print(output)

if __name__ == '__main__':
    run()