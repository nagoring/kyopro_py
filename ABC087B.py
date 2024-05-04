
if __name__ == '__main__':
    # 500
    a = int(input())
    # 100
    b = int(input())
    # 50
    c = int(input())
    # total
    x = int(input())
    A = 500
    B = 100
    C = 50

    _result = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if(A * i + B * j + C * k == x):
                    _result += 1

    print(_result)
