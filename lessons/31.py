# l = list('hello, world')
# print(l)

# s = ''.join(l)
# print(s)
# l = 'home,sweet,home'.split(',')
# print(l)
# list1 = list(range(1, 6))
# print(list1)
# list2 = list(range(6, 11))
# print(list2)
# list3 = list1 + list2
# print(list3)

# list1 = list(range(1, 11))
# print(list1)
# del list1
# list1.clear()
# print(list1)

import copy

list1 = list(range(1, 11))
list1.append([11, 12, 13])

# list2 = copy.deepcopy(list1)
# print(list2)
# print(list1)
# print(list2)
list2 = [i for i in list1]
list1[1] = 'a'
list1[10][0] = 'a'
print(list1)
print(list2)
