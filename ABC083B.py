if __name__ == '__main__':
    N, A, B = map(int,input().split(" "))
    n_keta = len(str(N))
    answer = 0
    for _i in range(N):
        i = _i + 1
        # print(f"loop:{i}")

        # 5桁まで
        if len(str(i)) == 1:
            if A <= i <= B:
                answer += i
        elif len(str(i)) == 2:
            sum_of_each_digit = int(str(i)[0]) + int(str(i)[1])
            if A <= sum_of_each_digit <= B:
                answer += i
        elif len(str(i)) == 3:
            sum_of_each_digit = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
            if A <= sum_of_each_digit <= B:
                answer += i
        elif len(str(i)) == 4:
            sum_of_each_digit = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
            if A <= sum_of_each_digit <= B:
                answer += i
        elif len(str(i)) == 5:
            sum_of_each_digit = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3]) + int(str(i)[4])
            if A <= sum_of_each_digit <= B:
                answer += i

    print(answer)
