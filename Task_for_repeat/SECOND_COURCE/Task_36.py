def merge(lst):
    result = {}
    for dic in lst:
        for key, item in dic.items():
            s = result.get(key, set())
            s.add(item)
            result[key] = s
    return result



lst = [{'a': 1, 'b': 2},
       {'b': 10, 'c': 100},
       {'a': 1, 'b': 17, 'c': 50},
       {'a': 5, 'd': 777}]
print(merge(lst))
