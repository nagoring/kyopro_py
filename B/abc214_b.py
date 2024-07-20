def run():
    S, T = map(int, input().split(" "))
    success_counter = 0
    for a in range(S + 1):
        for b in range(S + 1):
            for c in range(S + 1):
                if (a + b + c) <= S and (a * b * c) <= T:
                    success_counter += 1

    print(success_counter)

if __name__ == '__main__':
    run()
