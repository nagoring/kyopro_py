def run():
    N = int(input())
    output = 0
    for _ in range(N):
        name = input()
        if name == 'Takahashi':
            output += 1

    print(output)


if __name__ == '__main__':
    run()