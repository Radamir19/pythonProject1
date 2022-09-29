n = int(input())
a = []
max = 0
min = 10 ** 9
for i in range(2, n):
    if n % i == 0:
        b = []
        for j in range(2,i):
            if i % j == 0:
                b.append(j)
        if len(b) == 0:
            a.append(i)
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        i_max = i
    if a[i] < min:
        min = a[i]
        i_max = i
print(*a)
a[i_min], a[i_max] = a[i_max], a[i_min]
print(*a)

