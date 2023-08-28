ls_num = [int(i) for i in input().split()]
summa = sum(ls_num)
ls_str = [str(i) for i in ls_num]
print(f"{'+'.join(ls_str)}={summa}")
