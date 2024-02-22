
# dict4 = {**dict1, **dict2, **dict3}
# dict4 = dict1 | dict2 | dict3
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)

# print(num := 1)
# print(num)
# print(dict1)


# while (age := int(input('How old are you? '))) < 18 or age > 65:
#     print('Wrong age')
# else:
#     print('Ok')
# dict1 = {1: 10, 2: 20}
# dict2 = {3: 30, 4: 40}
# dict3 = {5: 50, 6: 60}
# d = {**dict2, **dict3}

# for key in (d := {**dict2, **dict3}):
#     dict1[key] = d[key]
# for key in dict3:
#     dict1[key] = dict3[key]

# print(dict1)

products = {
    'Sony': 110,
    'Samsung': 100,
    'LG': 95,
    'iPhone': 105,
}
# new_products = {}

print(products)


# for title, price in products.items():
#     if price >= 100:
#         new_products[title] = price


new_products = {title: '%.2f' % (price * 1.1) for title,
                price in products.items() if price > 100}
print(new_products)
