if __name__ == '__main__':
    N = int(input())
    a_array = list(map(int, input().split(" ")))
    Alice = 0
    Bob = 0
    a_array.sort(reverse=True)
    for i,number in enumerate(a_array):
        index = i + 1
        if index % 2 == 0:
            Bob += number
        else:
            Alice += number

    print(Alice - Bob)

