
def run():
    start = 1
    end = 2
    step = 0.1
    current = start
    while current <= end:
        print(round(calc(current), 2))
        current += step



def calc(x):
    return x * (10 - 2 * x) ** 2


if __name__ == '__main__':
    run()
