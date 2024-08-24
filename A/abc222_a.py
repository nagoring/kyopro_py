def run():
    N = input()
    size = len(N)
    if size == 4:
        print(N)
        return

    print(N.zfill(4))

if __name__ == '__main__':
    run()