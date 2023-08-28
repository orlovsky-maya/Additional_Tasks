l = [int(i) for i in input().split()]
m = [int(i) for i in input().split()]
for j in range(len(l)):
    l[j] += m[j]
print(*l)