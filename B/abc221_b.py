def run():
    S = input()
    T = input()

    if S == T:
        print("Yes")
        return

    for i in range(len(S) - 1):
        s = S[i]
        t = T[i]
        if s != t:
            swapped = T[:i] + T[i + 1] + T[i] + T[i+2:]

            if S == swapped:
                print("Yes")
                return
            else:
                print("No")
                return


if __name__ == '__main__':
    run()
