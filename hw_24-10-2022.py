def count_delit_na_dva(x):
    i = 0
    k = 0
    while i < x:
        if x % 2 == 0:
            k += 1
            x = x // 2
        i += 1
    return k

def find_deliteli(x):
    b = []
    for i in range(2,int(x ** 0.5)):
        if x % i == 0:
            b.append(i)
            b.append(x // i)
    return b

x = int(input("Введите число: "))
print(count_delit_na_dva(x))
print(find_deliteli(x))