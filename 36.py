# months = {
#     'jan': 'January',
# }
# print(f'{months}, {id(months)=}')
# months['feb'] = 'February'
# print(f'{months}, {id(months)=}')

# products = [
#     {'title': 'Samsung', 'price': 100},
#     {'title': 'Sony', 'price': 110},
# ]
# print(products[1]['title'])

# for product in products:
#     print(f'Title: {product["title"]}, Price: {product["price"]}')

# skills = [
#     {'who': 'Stas', 'skill': 'SQL'},
#     {'who': 'Wika', 'skill': 'Marketing'},
# ]
# for candidate in skills:
#     print(f'Person: {candidate["who"]}, Can do: {candidate["skill"]}')


# person = {
#     'first_name': 'John',
#     'last_name': 'Doe',
#     'age': 30,
#     'job': 'programmer',
#     'languages': ['Python', 'C#', 'PHP', 'JS']
# }
# print(person)

# Add items
# # person['city'] = 'Minsk'
# person.update({"city": "Minsk"})
# person.update({"age": 31})
# print(person)

# # Remove
# # del person['city']
# # print(person)
# if 'last_name2' in person:
#     print(f'deleted: {person.pop("last_name2")}')
# print(
#     f'deleted: {person.pop("last_name2", "There are not last_name2 element in dictionary")}')
# print(person)
# print(f' I have deleted: {person.popitem()} sir, Im very sorry')

# person.clear()
# print(person)

# person2 = person.copy()
# person2 = dict(person)
# person2['age'] = 40
# person2['languages'][0] = 'kuku'
# print(person)
# print(person2)

# Loop
# for key in person.keys():
#     print(f'{key=}, key value - {person[key]}')
#     if type(person[key]) is list:
#         print(f'LIST - {person[key]}')
#         for lang in person[key]:
#             print(lang, end=' ')

# for item in person.values():
#     print(item)
#     if item is list:
#         for lang in item:
#             print(lang, end=' ')

# for key, item in person.items():
#     print(f'{key=}, {item=}')


# dict3 = {**dict1, **dict2}
# dict3 = {}
# dict3.update(dict1)
# dict3.update(dict2)
# print(dict3)


# print('{x} | {y} | {z}'.format(x=dict1['a'], y=dict1['b'], z=dict1['c']))
# print('{a} | {b} | {c}'.format(**dict1))
# print(dict3)

# dict1 = dict1 | dict2
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'b': 5, 'e': 6}

dict1 |= dict2
# OR
dict1 = dict1 | dict2
print(dict1)
