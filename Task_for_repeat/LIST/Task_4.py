num = [i for i in input().split('-')]
if num[0] == '7':
    num = num[1:]

correct = True
for j in num:
    if len(num) != 3:
        correct = False
        break
    elif not j.isnumeric():
        correct = False
        break
    elif len(num[0]) != 3 or len(num[1]) != 3 or len(num[2]) != 4:
        correct = False
        break

if correct:
    print('YES')
else:
    print('NO')

number = [i for i in input().split('-')]
if number[0] == '7':
    del number[0]
if len(number[0]) == 3 and len(number[1]) == 3 and len(number[2]) == 4:
    numbers_st = ''.join(number)
    if numbers_st.isdigit():
        print('YES')
    else:
        print('NO')
else:
    print('NO')