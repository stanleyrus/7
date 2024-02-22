list1 = list(range(1, 11))
print(list1)
# MODIFYING LIST
# list1[0] = 'test'
# print(list1)
# list1[-1] *= 5
# print(list1)

# # list1[:3] = ['ttt'] * 3
# list1[:3] = list(range(3))
# print(list1)

# ADDING ELEMENTS
# list1.append('new el 1')
# print(list1)

# list1.insert(2, 'new el 2')
# print(list1)

# list1[1] = 'new el 3'
# print(list1)

# list1.insert(len(list1), 'new el 3')
# print(list1)

# REMOVING ELEMENTS
# del list1[-1]
# print(list1)
# del list1[len(list1) - 1]
# # del list1
# print(list1)

# last_el = list1.pop()
# print(list1, last_el)

# el = list1.pop(-2)
# print(list1, el)

# list1[1:4] = ['new_el_1', 'new el 2', 'new el 3']
# print(list1)

# if 'new el 2' in list1:
#     list1.remove('new el 2')
# print(list1)

# if 'new el 2' in list1:
#     list1.remove('new el 2')
# print(list1)

months = [
    ['december', 'january', 'february'],
    ['march', 'april', 'may'],
    ['june', 'july', 'august'],
    ['september', 'november', 'december']
]
print(months)
print(months[1][2])
