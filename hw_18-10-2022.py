for i in range(256):
    n = i
    s = bin(n)[2:]
    s = s.zfill(8)
    s1 = ''
    for i in range(len(s)):
        if s[i] == '0':
            s1 += '1'
        elif s[i] == '1':
            s1 += '0'
    r = int(s1, 2)
    print(r - n)


