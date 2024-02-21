# list1 = [1, 2, 3]

# list1 = list(map(lambda x: x + 5, list1))



# list1 = list(range(1, 11))


# list2 = list(filter(lambda x: x % 2 == 0, list1))

# print(list2)


# print(list1)

# for i, el in enumerate(list1):
#     list1[i] = el * 2


# list1 = [i * 2 for i in list1]
# print(list1)

# # iterator = map(fn, list)
# list1 = [1, 2, 3]


# def get_double(x: int) -> int:
#     return x * 2


# list1 = tuple(map(lambda x: x * 2, list1))


# print(list1)


# list2 = list(range(1, 11))
# # # list2 = [x for x in list2 if x % 2 == 0]
# # # print(list2)

# # # filter(fn, list)
# # print(list2)


# def doubler(x):
#     return x % 2 == 0


# def anti_doubler(x):
#     return x % 2 != 0



# list3 = list(filter(doubler, list2))

# list2 = list(filter(doubler, list2))


# print(list2)
# print(list3)
# # list4 = list(filter(lambda x: x % 2 == 0, list2))


# num_list = [1, 2, 3]
# str_list = ['one', 'two', 'three']
# res_list = list(zip(num_list, str_list, strict=True))
# res_dict = dict(zip(num_list, str_list))
# # print(res_list)
# print(res_dict)


# a, b = zip(*res_list)
# print(a)
# print(b)

num_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
res_list = list(zip(num_list, str_list, strict=True))
res_dict = dict(zip(str_list, num_list))
c = list(zip(*res_dict, strict=True))
d = list(zip(*res_dict.items()))
print(f'{c = }')
print(d)
