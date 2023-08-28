def merge(lst):
    result = {}
    for i in lst:
        for key, values in i.items():
            result[key] = result.get(key, set())
            result[key].add(values)
    return result

result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100},
                {'a': 1, 'b': 17, 'c': 50},
                {'a': 5, 'd': 777}])
print(result)

