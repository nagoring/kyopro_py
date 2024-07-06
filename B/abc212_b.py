def run():
    X = input()
    # ゾロ目チェック
    if X[0] == X[1] == X[2] == X[3]:
        print("Weak")
        return
    y = [0, 0, 0, 0]
    y[0] = int(X[0])
    y[1] = int(X[1])
    y[2] = int(X[2])
    y[3] = int(X[3])

    # 連番チェック
    snum = 0
    for i in range(3):
        a = y[i]
        b = y[(i + 1) % 4]

        if (a + 1) % 10 == b:
            snum += 1

        if snum == 3:
            print("Weak")
            return

    print("Strong")


if __name__ == '__main__':
    run()
