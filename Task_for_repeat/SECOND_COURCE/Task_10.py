named_cities = {input() for _ in range(int(input()))}
city = input()
if city not in named_cities:
    print('OK')
    named_cities.add(city)
else:
    print('REPEAT')