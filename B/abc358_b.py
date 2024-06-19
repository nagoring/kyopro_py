def run():
    # N, A_sec = map(int, "3 4".split(" "))
    N, A_sec = map(int, input().split(" "))
    # times = list(map(int, "0 2 10".split(" ")))
    times = list(map(int, input().split(" ")))

    current_sec = 0
    for i in range(N):
        time = times[i] - current_sec
        if time < 0:
            time = 0
        current_sec += time
        current_sec += A_sec
        print(f"{current_sec}")



if __name__ == '__main__':
    run()
