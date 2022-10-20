def check_is_simple(x):
    k = 0
    for i in range(2,x):
        if x % i == 0:
            k += 1
    if k == 0:
        return "YES"
    else:
        return "NO"

print(check_is_simple(18))