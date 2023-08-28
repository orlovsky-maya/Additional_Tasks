s = input()
ind_1 = s.find('h')
ind_2 = s.rfind('h')
sub_str = s[ind_1 + 1:ind_2]
print(s[:ind_1 + 1] + sub_str[::-1] + s[ind_2:])
