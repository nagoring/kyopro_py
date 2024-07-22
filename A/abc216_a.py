def run():
    X, Y = map(int, input().split("."))
    if 0 <= Y <= 2:
        print(f"{X}-")
    elif 3 <= Y <= 6:
        print(f"{X}")
    elif 7 <= Y <= 9:
        print(f"{X}+")


if __name__ == '__main__':
    run()
