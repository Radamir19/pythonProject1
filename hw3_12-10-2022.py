s = input()

f_count = s.count('f')

if f_count == 0:
    print(-2)
if f_count == 1:
    print(-1)
if f_count >= 2:
    f1 = s.find("f")
    f2 = s.rfind("f")
    print(f1,f2)#
