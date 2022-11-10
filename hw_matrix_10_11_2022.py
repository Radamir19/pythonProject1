def pr():
    for i in range(len(b)):
        print(*b[i])

n, m = map(int, input().split())
b = []
for i in range(n):
    b.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            b[i].append(".")
        else:
            b[i].append("*")

pr()##