numbers = [int(num) for num in input().split()]
counter = 0
current_num = numbers[0]
for n in range(1, len(numbers)):
    if numbers[n] > current_num:
        counter += 1
        current_num = n
print(counter)
