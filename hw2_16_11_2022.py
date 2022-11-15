from random import randint, seed

seed(0)
n, m = map(int, input().split())
m = [[randint(100, 999) for _ in range(m)] for _ in range(n)]
for i in range(len(m)):
    print(*m[i])
for i in range(len(m)):
    print("Максимальный элемент в " + str(i + 1) + "-ой строчке равен: " + str(max(m[i])))
