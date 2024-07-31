X = input()
N = int(input())
S = [input() for _ in range(N)]

pos = {c: i for i, c in enumerate(X)}
S.sort(key=lambda s: [pos[c] for c in s])

print(*S, sep="\n")