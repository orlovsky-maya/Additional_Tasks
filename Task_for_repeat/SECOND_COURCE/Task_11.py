s = input().split()
dictionary = {}
for elem in s:
    dictionary[elem] = dictionary.get(elem, 0) + 1
    print(dictionary[elem], end=' ')