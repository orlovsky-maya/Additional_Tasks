def build_query_string(dictionary):
    result_text = []
    for key, value in dictionary.items():
        result_text.append(f'{key}={value}')
    result_text.sort()
    return '&'.join(result_text)


print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
