def run():
    input_array = map(int, input().split(" "))
    abc_array = []
    for i in (range(97, 123)):
        abc_array.append(chr(i))

    result = ""
    for i in input_array:
        result += abc_array[i - 1]

    print(result)

if __name__ == '__main__':
    run()