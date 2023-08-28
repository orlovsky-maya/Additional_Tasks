s = input()
lenght = len(s)
rub = lenght * 60 // 100
kop = lenght * 60 % 100
print(f'{rub} р. {kop} коп.')