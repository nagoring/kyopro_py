def run():
    S1 = input()
    S2 = input()
    S3 = input()
    T = input()
    s_array = [S1, S2, S3]
    result = ""
    for _i in T:
        i = int(_i)
        result += s_array[i - 1]

    print(result)

if __name__ == '__main__':
    run()
