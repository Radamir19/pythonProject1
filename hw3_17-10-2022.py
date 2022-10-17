for i in range(101):
    n = i
    s = bin(n)[2:]
    s = s[-1::-1]
    res = int(s, 2)
    if res == 13:
        print(n)
        break