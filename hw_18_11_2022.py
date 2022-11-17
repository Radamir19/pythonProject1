n = 5
m = [["." for _ in range(n)] for _ in range(n)]
for i in m:
    print(*i)
print("-" * 20)
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            m[i][j] = 0
        if i + j == n - 1:
            m[i][j] = 1
        if i + j > n - 1:
            m[i][j] = 2
for i in m:
    print(*i)