animals = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык',
           'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь',
           'Овца']
year = int(input())
ind = year % 12
print(animals[ind])