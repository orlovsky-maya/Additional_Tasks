numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991,
           908, 8976, 6565, 5665, 10, 1000, 908,
           909, 232, 45654, 786]
result = list(filter(lambda num: num != num[::-1], map(lambda num: str(num), numbers)))
print(*result)