a = [5,6,7,8,9]
for i in range(2,101):
    a = [j for j in a if (j==i or j%i!=0)]
print(*a)