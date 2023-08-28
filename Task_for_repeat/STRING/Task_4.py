s = input()
counter = s.count('f')
if counter == 0:
    print('-2')
elif counter == 1:
    print('-1')
else:
    ind_1 = s.find('f')
    print(s.find('f', ind_1 + 1))
