def run():
    A, B, C = map(int, input().split(" "))
    # A, B, C = 401, 599, 200

    index = 1
    for num in range(A, B+1):
        res = C * index
        if A <= res <= B:
            print(res)
            return
        index += 1


    print(-1)




if __name__ == '__main__':
    run()
