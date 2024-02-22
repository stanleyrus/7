# colors_list = ['red', 'black', 'white', 'green']
# colors_touple = ('red', 'black', 'white', 'green')

# red, black, white, green = colors_list
# print(red, black, white, green)
# red2, black2, white2, green2 = colors_touple
# print(red2, black2, white2, green2)
# colors_list = ['red', 'black', 'white', 'green']
# red, black, *other_colors = colors_list

# print(red, black, other_colors)

# t1 = 1, 10
# # print(type(t1), t1)
# # print(range(*t1))
# # for i in range(*t1):
# #     print(i, end=' ')
# t1 = 1, 10
# print([*range(*t1)])
# colors_list = ['red', 'black', 'white', 'green']
# colors_touple = ('red', 'black', 'white', 'green')

# (*red,), black, *other_colors = colors_touple
# print(red, black, other_colors)

# (*l,) = 'hello'
# # print(l)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# # l3 = l1 + l2

# # OR

# l3 = [*l1, *l2]

# print(l3)

# d1 = {'a': 1, 'b': 2, 'c': 3}
# # d2 = d1.copy()
# d2 = {**d1}

# print(d1, id(d1))
# print(d2, id(d2))
# print(d1 is d2)

# colors_d = {'red': 'красный', 'black': 'черный',
#             'white': 'белый', 'green': 'зеленый'}
# # a, *b = colors_d.keys()
# a, *b = colors_d.items()
# # print(a, b)
# s = {'red', 'black', 'white', 'green'}
# a, *b = s
# print(a, b)

s = {'one', 'two', 'three'}
t = (4, 10)
l = [True, False, 5.4]
res = [*s, *t, *range(*t), *l]
print(res)
