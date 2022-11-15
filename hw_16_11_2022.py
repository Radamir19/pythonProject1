def pr():
    print("-" * 20)
    for i in range(n):
        print(*m[i])

n = int(input())
m = [["." for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            m[i][j] = "*"
pr()

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            m[i][j] = "*"
pr()

for i in range(n):
    for j in range(n):
        if i == n // 2:
            m[i][j] = "*"
pr()

for i in range(n):
    for j in range(n):
        if j == n // 2:
            m[i][j] = "*"
pr()
