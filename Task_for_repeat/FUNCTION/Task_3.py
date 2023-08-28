def is_magic(date):
    date_lst = date.split('.')
    multiplication = int(date_lst[0]) * int(date_lst[1])
    last_digits = date_lst[2][-2:]
    if multiplication == int(last_digits):
        return True
    else:
        return False

print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))

print(is_magic('15.03.1945'))
print(is_magic('03.11.2033'))
print(is_magic('03.11.2032'))
print(is_magic('15.12.1234'))
print(is_magic('10.09.1990'))