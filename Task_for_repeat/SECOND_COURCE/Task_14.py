letters = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
           2: ['D', 'G'],
           3: ['B','C', 'M', 'P'],
           4: ['F', 'H', 'V', 'W', 'Y'],
           5: ['K'],
           8: ['J', 'X'],
           10: ['Q', 'Z']}

word = input()
counter = 0
for c in word:
    for key, values in letters.items():
        if c in values:
            counter += key
            break

print(counter)
