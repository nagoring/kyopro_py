def is_even(in_array):
    a = in_array.copy()
    for val in a:
        if val == 0:
            return False
        if val % 2 != 0:
            return False

    return True


def exec(current_a):
    result = 0
    while (1):
        a = current_a[:]
        for val in a:
            if not is_even(a):
                return result

            if val % 2 == 0:
                result += 1
                break
        current_a = (int(x / 2) for x in current_a)
        current_a = list(current_a)


if __name__ == '__main__':
    number_length = int(input())
    _a = [int(x) for x in input().split()]

    last_result = exec(_a)

    print(last_result)
