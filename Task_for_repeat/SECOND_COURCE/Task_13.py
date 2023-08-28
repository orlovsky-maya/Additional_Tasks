m = int(input())
n = int(input())
home_libr = {input() for _ in range(m)}
summer_lst = [input() for _ in range(n)]
for book in summer_lst:
    if book in home_libr:
        print('YES')
    else:
        print('NO')