# list1 = [1] * 3 + [2] + [3] * 5 + [0] * 2
# print(list1, list1.count(1))
# list1 += list('hello')
# print(list1, list1.count('l'))
# list1 += [True] * 2 + [False] * 3
# print(list1)
# print(list1, list1.count('1'))

# list1 = list(range(5))
# print(list1)
# # list1 += ['test1', 'test2']
# s = 'test1', 'test2'
# list1.extend(s)
# print(list1)

list1 = [1] * 3 + [2] + [3] * 5 + [0] * 2
list1 += [True] * 2 + [False] * 3
print(list1)

# list1.sort(reverse=True)
# print(list1)
print(sorted(list1, reverse=True))
print(list1)
