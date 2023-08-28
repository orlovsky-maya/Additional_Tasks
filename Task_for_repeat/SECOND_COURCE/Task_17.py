first_lst = {int(i) for i in input().split()}
second_lst = {int(i) for i in input().split()}
result_lst = first_lst.intersection(second_lst)
if len(result_lst) == 0:
    print('BAD DAY')
else:
    print(*sorted(result_lst, reverse=True))