num = input()
if len(num) == 5:
    num = num[::-1]
    print(num.lstrip('0'))
else:
    last_part = num[1:][::-1]
    print(num[0] + last_part)
