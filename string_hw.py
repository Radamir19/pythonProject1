a = ['zero','one','two','three']
s = '1 + 2 = 3'
print(s)
for i in range(len(a)):
    if str(i) in s:
        s = s.replace(str(i),a[i])
print(s)