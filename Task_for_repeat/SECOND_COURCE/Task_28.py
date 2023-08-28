n = int(input())
dots = [input().split() for _ in range(n)]
my_dict = {'Первая четверть': 0,
           'Вторая четверть': 0,
           'Третья четверть': 0,
           'Четвертая четверть': 0}
for dot in dots:
    if int(dot[0]) > 0 and int(dot[1]) > 0:
        my_dict['Первая четверть'] = my_dict.get('Первая четверть', 0) + 1
    elif int(dot[0]) > 0 and int(dot[1]) < 0:
        my_dict['Четвертая четверть'] = my_dict.get('Четвертая четверть', 0) + 1
    elif int(dot[0]) < 0 and int(dot[1]) > 0:
        my_dict['Вторая четверть'] = my_dict.get('Вторая четверть', 0) + 1
    elif int(dot[0]) < 0 and int(dot[1]) < 0:
        my_dict['Третья четверть'] = my_dict.get('Третья четверть', 0) + 1

for keys, values in my_dict.items():
    print(f'{keys}: {values}')
