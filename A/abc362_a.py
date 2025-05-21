def run():
    # R = 20
    # G = 30
    # B = 10
    # C = "Red"
    R,G,B = map(int, input().split(" "))
    C = input()

    if C == "Red":
        print(min(G,B))
        return

    if C == "Green":
        print(min(R,B))
        return

    #Blue
    print(min(R,G))



if __name__ == '__main__':
    run()