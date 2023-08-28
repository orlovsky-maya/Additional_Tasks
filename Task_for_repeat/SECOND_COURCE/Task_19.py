from functools import reduce
from operator import *


def product_of_odds(data):
    filtered_lst = filter(lambda num: mod(num, 2), data)
    mult = reduce(lambda num1, num2: mul(num1, num2), filtered_lst, 1)
    return mult


lst = [1, 2, 3, 4, 5]
print(product_of_odds(lst))
