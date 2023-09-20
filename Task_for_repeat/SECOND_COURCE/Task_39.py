with open('words.txt', 'r', encoding='utf-8') as file:
    txt = file.read().split()
    largest_words = []
    sorted_lts = sorted(txt, key=lambda word: len(word), reverse=True)
    max_letter = len(sorted_lts[0])
    for word in sorted_lts:
        if len(word) == max_letter:
            largest_words.append(word)
    print(*largest_words, sep='\n')

