file_name = input()
with open(file_name, 'r', encoding='utf=8') as file:
    text = file.readlines()
    print(len(text))