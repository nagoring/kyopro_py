def run():
    N = int(input())
    easy = 40
    normal = 70
    hard = 90
    lunatic = 100
    if N < easy:
        print(easy - N)
        return
    if N < normal:
        print(normal - N)
        return
    if N < hard:
        print(hard - N)
        return
    if N <= lunatic:
        print("expert")



    print()
if __name__ == '__main__':
    run()