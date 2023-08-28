def get_shipping_cost(quantity):
    first_shipping = 1000
    for i in range(1, quantity):
        if quantity == 1:
            return first_shipping
        else:
            first_shipping += 120
    return first_shipping

print(get_shipping_cost(1))
print(get_shipping_cost(3))
print(get_shipping_cost(2))
print(get_shipping_cost(100))
print(get_shipping_cost(41))


# объявление функции
def get_shipping_cost(quantity):
        return 1000 + ((quantity - 1) * 120)
# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))
