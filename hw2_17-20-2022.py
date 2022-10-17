for i in range(2, 2000):
    n = i
    s = bin(n)[2:]
    s = s[:-1]
    if n % 2 != 0:
        s += '10'
    else:
        s += '01'
    res = int(s, 2)
    if res == 2018:
        print(n)
        break