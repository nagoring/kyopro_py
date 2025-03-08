def run():
    s = input()
    first = s[0]
    second = s[1]
    third = s[2]
    r_index = 0
    m_index = 0
    s_index = 0
    index = 0
    for c in s:
        index = index + 1
        if c == "R":
            r_index = index
        if c == "M":
            m_index = index
        if c == "S":
            s_index = index


    if r_index < m_index:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    run()