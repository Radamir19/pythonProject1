from random import randint

n, m = 4, 5
M = [[randint(-5, 10) for _ in range(m)] for _ in range(n)]
for i in M:
    print(*i)

k = 0
b = []
for j in range(m):
    for i in range(n):
        if M[i][j] >= 0:
            k += 1
    if k > m // 2:
        b.append(j)
    k = 0

print("Номера столбцов, где количество элементов более половины: " + str(b))
