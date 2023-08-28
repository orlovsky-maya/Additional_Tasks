access_dict = {'execute': 'X',
               'read': 'R',
               'write': 'W'}
files_name = {lst[0]: lst[1:] for lst in [input().split() for _ in range(int(input()))]}
requests = [input().split() for _ in range(int(input()))]

for l in requests:
    if access_dict[l[0]] in files_name[l[1]]:
        print('OK')
    else:
        print('Access denied')
