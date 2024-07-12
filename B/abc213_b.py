def run():
    N = int(input())
    A = list(map(int, input().split()))
    # N = 5
    # A = list(map(int, "3 1 4 15 9".split()))
    a_dict = {i + 1: A[i] for i in range(N)}
    items = a_dict.items()
    sorted_items = sorted(items, key=lambda item: item[1], reverse=True)
    key2, value2 = sorted_items[1]
    sorted_by_values = dict(sorted_items)
    # print(sorted_by_values)
    print(key2)
    # dict = sorted(dict)
    # # A.sort(reverse=True)
    # print(dict)



if __name__ == '__main__':
    run()
