import copy
def run():
    origin = [1, 2, 3]
    origin_copy = copy.copy(origin)
    input_array = list(map(int, input().split(" ")))
    if input_array[0] == input_array[1]:
        print("-1")
        return

    for i in origin:
        for j in input_array:
            if i == j:
                origin_copy.remove(i)

    print(origin_copy[0])


if __name__ == '__main__':
    run()


# a, b = map(int, input().split())
#
# if a == b:
#     print("-1")
# else:
#     print(6 - a - b)
# 1. 総和の性質 (Sum Property)
# 整数の集合の総和（この場合、候補者の番号の総和）を利用して、残りの要素を見つける方法です。全体の合計から一部の要素の合計を引くことで、残りの要素を見つけるという考え方です。
#
# 2. 補数の概念 (Complement)
# 補数とは、全体の集合から特定の部分集合を引いた残りの部分を指します。この場合、候補者全体から犯人でないとわかっている部分集合を引くことで、犯人を特定する方法です。
#
# これらの概念は、数理的には以下のように説明されます：
#
# 全体の集合 S の要素の総和を T とする。
# 部分集合 A の要素の総和を S_A とする。
# 補集合 S\A の要素の総和は T - S_A となる。
# 具体的な例を挙げると：
#
# 候補者が 1, 2, 3 の場合、全体の総和 T は 1 + 2 + 3 = 6 です。
# 目撃者が覚えている「犯人でない」人物 a と b の総和 S_A は a + b です。
# 犯人は補集合 S\A の要素であり、その総和は T - S_A = 6 - (a + b) となります。
# このようにして、補数や総和の性質を利用することで、犯人を特定することができます。