a = input().split()


def maximum():
    m = 0
    for i in range(len(a)):
        x = a[i]
        for j in range(i + 1, len(a)):
            y = a[j]
            if int(x) > int(y):
                if int(x) > m:
                    m = int(x)
            else:
                if int(y) > m:
                    m = int(y)
    return str(m)


def minimum():
    m_i = 10 ** 9
    for i in range(len(a)):
        x1 = a[i]
        for j in range(i, len(a)):
            y1 = a[j]
            if int(x1) < int(y1):
                if int(x1) < m_i:
                    m_i = int(x1)
            else:
                if int(y1) < m_i:
                    m_i = int(x1)
    return str(m_i)


maximum()

minimum()

m_i_n = a.index(minimum())
m_a_x = a.index(maximum())
a[m_i_n], a[m_a_x] = a[m_a_x], a[m_i_n]
print(*a)