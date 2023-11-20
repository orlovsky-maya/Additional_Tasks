words = [input() for i in range(int(input()))]
for word in words:
    if len(word) > 10:
        length = len(word[1:-1])
        print(f'{word[0]}{length}{word[-1]}')
    else:
        print(word)