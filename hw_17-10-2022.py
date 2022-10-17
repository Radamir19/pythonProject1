for i in range(1000, 100, -1):
    n = str(i)
    m = 0
    s = ''

    s1 = int(n[0]) * int(n[1])
    s2 = int(n[1]) * int(n[2])
    first = min(s1, s2)
    second = max(s1, s2)
    s = str(first) + str(second)
    if s == '621':
        print(n)
        break

