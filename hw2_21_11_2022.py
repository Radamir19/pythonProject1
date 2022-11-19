from random import randint

n, m = 8, 5
M = [[randint(20, 40) for _ in range(m)] for _ in range(n)]
for i in M:
    print(*i)

b = []
k = 0
for i in range(n):
    for j in range(m):
        if M[i][j] % 2 == 0:
            k += 1
    if k >= 2:
        b.append(i)
    k = 0
print("Номера строк, содержащих не менее 2-х четных чисел: " + str(b))