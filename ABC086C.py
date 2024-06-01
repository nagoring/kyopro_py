def run():
    N = int(input().strip())
    # N = 1

    travel_plan = []
    for _ in range(N):
        travel_plan.append(input().strip())

    # travel_plan = ["2 1 1"]

    current_t, current_x, current_y = 0, 0, 0

    for i in range(N):
        _input = travel_plan[i]
        t, x, y = map(int, _input.split(" "))

        # マンハッタン距離
        distance = abs(x - current_x) + abs(y - current_y)
        t_diff = t - current_t

        if t_diff < distance:
            print("No")
            return

        if (t_diff % 2) != (distance % 2):
            print("No")
            return

        current_t, current_x, current_y = t, x, y

    print("Yes")


if __name__ == '__main__':
    run()
