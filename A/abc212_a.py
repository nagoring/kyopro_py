def run():
    A, B = input().split(" ")
    A = int(A)
    B = int(B)

    if 0 < A and B == 0:
        print("Gold")
        return
    if A == 0 and 0 < B:
        print("Silver")
        return

    print("Alloy")

if __name__ == '__main__':
    run()