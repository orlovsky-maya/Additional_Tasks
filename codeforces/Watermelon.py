w = int(input())


def is_even(num):
    return num % 2 == 0


flag = False
for i in range(2, w, 2):
    part = w - i
    if is_even(part):
        flag = True
        break

if flag == True:
    print("YES")
else:
    print("NO")
