def run():
    N = input()
    # a_array = list(map(int, "4 3 2 3 2 1 4 1".split(" ")))
    a_array = list(map(int, input().split(" ")))
    result = 0

    for i in range(len(a_array) - 2):
        left = a_array[i]
        center = a_array[i + 1]
        right = a_array[i + 2]
        if left == right and center != left:
            result += 1

    print(result)
if __name__ == '__main__':
    run()
