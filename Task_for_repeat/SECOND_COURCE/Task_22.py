n = input()[::-1]
length = len(n)
result = []
counter = 0
for i in range(length):
    result.append(n[i])
    counter += 1
    if counter == 3:
        result.append(',')
        counter = 0
if result[-1] == ',':
    del result[-1]
result.reverse()
print(*result, sep='')




