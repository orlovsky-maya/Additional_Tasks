s = [i for i in input().split()]
n = int(input())
result_list = []

for k in range(n):
    temp_lst = []
    for j in range(k, len(s), n):
        temp_lst.append(s[j])
    result_list.append(temp_lst)

print(result_list)


