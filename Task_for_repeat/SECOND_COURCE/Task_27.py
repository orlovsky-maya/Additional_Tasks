with open('ledger.txt', 'r', encoding='utf-8') as file:
    files_data = file.readlines()
    file_digits = list(map(lambda line: int(line.rstrip().lstrip('$')), files_data))
    print(f'${sum(file_digits)}')

