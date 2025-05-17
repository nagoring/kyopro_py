def run():
    # N = 4
    # K = 3
    # X = 777
    #     A = [2,3,5,11]
    N,K,X = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))
    B = []
    insertion_index = K

    for i in range(N):
        if i == insertion_index:
            B.append(X)
        B.append(A[i])

    if len(B) == N:
        B.append(X)

    print(*B)




if __name__ == '__main__':
    run()