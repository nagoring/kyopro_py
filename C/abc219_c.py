def create_sort_key(x_dict):
    def sort_func(s_array):
        ret = []
        for c in s_array:
            ret.append(x_dict[c])
        return ret

    return sort_func


def run():
    X = input()
    N = int(input())
    s_array = [input() for _ in range(N)]

    # 順序辞書生成
    x_dict = {}
    for i, c in enumerate(X):
        x_dict[c] = i

    s_array.sort(key=create_sort_key(x_dict))

    print(*s_array, sep="\n")


if __name__ == '__main__':
    run()
