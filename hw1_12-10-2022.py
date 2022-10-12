s = input()
if ' ' in s:
    s = s.replace(' ', '')
    if (s == s[-1::-1]):
        print("YES")
else:
    print("NO")