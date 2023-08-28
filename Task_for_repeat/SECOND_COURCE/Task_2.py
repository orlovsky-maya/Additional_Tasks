weight = float(input())
height = float(input())
body_mass_index = weight / (height * height)
if body_mass_index < 18.5:
    print('Недостаточная масса')
elif body_mass_index > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')