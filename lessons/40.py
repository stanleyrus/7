# set1 = set()
# print(set1, type(set1), id(set1))

# set2 = {1, 2, 3, 100}
# print(set2, type(set2), id(set2))

# set1.add('hell')
# print(set1, type(set1), id(set1))

# set1.update({2, 3, 4, 5, 'hello', 'world'})
# print(set1, type(set1), id(set1))


# # print(set1.pop())
# # print(set1, type(set1), id(set1))

# # if 'hello' in set1:
# #     set1.remove('hello')

# # set1.discard(2)
# # print(set1, type(set1), id(set1))

# print(set1, type(set1), id(set1))

# for i in set1:
#     print(i, end=' ')

# set3 = {1, 1, 2, 3, 3, 4, 3}
# print(set3)

list1 = [1, 1, 2, 3, 3, 4, 3]
print(list1)
list1 = list(set(list1))
print(list1)

set4 = {1, 2, 3}
print(set4, type(set4))
set4.add(4)
print(set4, type(set4))

set_f = frozenset(set4)
print(set_f, type(set_f))
set_f.add(5)
