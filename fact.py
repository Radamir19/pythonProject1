def fact(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return fact(x - 1) * x

print(fact(5))