from random import randint

n = 5
m = [[randint(19, 49) for _ in range(n)] for _ in range(n)]
for i in m:
    print(*i)

sr_ar = 0
summa = 0
k = 0
b = []
for j in range(n):
    for i in range(n):
        if m[i][j] % 2 != 0:
            summa += m[i][j]
            k += 1
    sr_ar = summa // k
    b.append(sr_ar)
    sr_ar = 0
    summa = 0
    k = 0

print("Среднее арифметическое нечетных элементов каждого столбца: "+str(b))
