s = [i for i in input().split()]
largest = len(s[0])
for j in s:
    if len(j) > largest:
        largest = len(j)
print(largest)

s = [len(i) for i in input().split()]
print(max(s))