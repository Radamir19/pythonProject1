n = int(input())
a = []
max = 0
min = 10 ** 9
for i in range(2, n):
    if n % i == 0:
        a.append(i)
for i in range(len(a)):
    if a[i] > max:
        max = i
    if a[i] < min:
        min = i
print(*a)
a[min], a[max] = a[max], a[min]
print(*a)

