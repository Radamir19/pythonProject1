k = 0
for i in range(1000):
    n = i
    s = bin(n)[2:]
    summary = sum(map(int, list(s)))
    if summary % 2 == 0:
        first = s.find('1')
        s1 = s[:first] + s[first + 1:]
    else:
        s1 = s.replace('0', '')
        s1 += '1'
    s2 = bin(int(s1, 2))[2:]
    summary2 = sum(map(int, list(s2)))
    if summary2 % 2 == 0:
        first = s2.find('1')
        s2 = s2[:first] + s2[first + 1:]
    else:
        s2 = s2.replace('0', '')
        s2 += '1'
    r = int(s2, 2)
    if r == 7:
        k += 1
print(k)