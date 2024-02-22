# list1 = [1, -2, 3, -4, 5]
# print([-i for i in list1])


# # list1 = []
# # list2 = [i for i in list1]
# # print(list2)

# x = 0
# y = 0
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

# for i in list1:
#     if i > 0:
#         x += 1
#     if i < 0:
#         y += i
# print([x, y])


# list1 = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
# while x < len(list1):
#     if int(list1[x]) > 0:
#         y += 1
#     x += 1
# print(y)

# while n < len(list1):
#     if int(list1[n]) < 0:
#         z += int(list1[n])
#     n += 1
# print(z)

# list2 = [y, z]
# print(list2)

# for i in range(len(list1)):
#     if int(list1[i]) > 0:
#         x += 1
#     if int(list1[i]) < 0:
#         y += int(list1[i])
# list2 = [x, y]
# print(list2)


# list2 = list(range(1, 11))
# list3 = [list2[0]]
# print(list2)
# for i in range(1, len(list2)):
#     if i % 2 == 0:
#         list3.append(list2[i])
# list2 = list3
# print(list2)
# x = 1
# list2 = list(range(1, 11))
# list3 = list2.copy()
# print(list3)
# while x < len(list2):
#     if x % 2 == 0:
#         del list3[x]
#     x += 1
# print(list3)

# OR

# list2 = [[1, 2]]
# list3 = list2[::2]
# list2 = list3
# print(list2)


# OR

list2 = list(range(1, 11))
print([e for i, e in enumerate(list2) if not i % 2])
