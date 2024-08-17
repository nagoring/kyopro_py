def run():
    POWER = 32
    A, B = map(int, input().split(" "))
    diff = A - B
    if diff == 0:
        print("1")
        return

    print(POWER ** diff)

if __name__ == '__main__':
    run()