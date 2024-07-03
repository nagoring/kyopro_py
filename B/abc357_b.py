def run():
    S = input()
    lower_counter = 0
    upper_counter = 0
    for c in S:
        if c.islower() :
            lower_counter += 1
        elif c.isupper() :
            upper_counter += 1

    if lower_counter > upper_counter:
        print(S.lower())
        return
    if lower_counter < upper_counter:
        print(S.upper())
        return

if __name__ == '__main__':
    run()