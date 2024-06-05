def run():
    N, L, R = map(int, input().split(" "))
    # N, L, R = map(int, "10 1 10".split(" "))
    all_array = list(range(1, N + 1))
    reverse_array = list(range(L, R + 1))
    reverse_array.reverse()
    begin_index = 0
    end_index = 0
    for i in all_array:
        if i == L:
            begin_index = L
        if i == R:
            end_index = R

    output_array = all_array
    reverse_index = 0

    for i in range(1, N + 1):
        if begin_index <= i <= end_index:
            output_array[i - 1] = reverse_array[reverse_index]
            reverse_index += 1
            continue

    output = " ".join(map(str, output_array))
    print(output)


if __name__ == '__main__':
    run()

#別解
# N, L, R = map(int, input().split())
#
# D = [i + 1 for i in range(N)]
# D[L - 1:R] = list(reversed(D[L - 1:R]))
#
# print(*D)
