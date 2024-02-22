
# # s[0] = 't'
# s = 'Hello'
# l1 = list(s)
# print(l1)
# print(l1[0])
# l1[0] = 't'
# print(l1)

# # ACCESSING ELEMENTS

# print(list1)
# print(list1[0])
# print(list1[len(list1)-1])
# list1 = list(range(1, 11))
# print(list1[-2::-1])
# list1 = list(range(1, 11))
# i = 0
# while i < len(list1):
#     print(list1[i], end=' ')
#     i += 1
# for i in list1:
#     print(i, end=' ')

# for i in range(len(list1)):
#     print(list1[i], end=' ')
# list2 = list('hello')
# for i in range(len(list2)):
#     print(f'{i} : {list2[i]}')

# [print(i, end=' ') for i in list1]
# l2 = [i for i in list1]
# print(l2)

list2 = list('hello')
for index, element in enumerate(list2):
    print(f'{index} : {element}')
