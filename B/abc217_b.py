def run():
    const_list = ["ABC", "ARC", "AGC", "AHC"]
    for i in range(3):
        const_list.remove(input())
    print(const_list[0])

if __name__ == '__main__':
    run()