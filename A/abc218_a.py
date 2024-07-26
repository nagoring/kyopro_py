def run():
    N = int(input())
    S = input()
    for i in range(len(S)):
        if (N - 1) == i:
            if S[i] == "o":
                print("Yes")
            else:
                print("No")


    print()

if __name__ == '__main__':
    run()