# list1 = ['a', 'b', 'a', 'c', 'c']
# res = []
# for i in list1:
#     if i not in res:
#         res.append(i)
# list1 = res.copy()
# print(list1)

# res = []
# [res.append(i) for i in list1 if i not in res]
# list1 = res.copy()
# print(list1)

# list1 = list(dict.fromkeys(list1))
# print(list1)

# list1 = list(set(list1))
# set1 = set(list1)
# dict1 = {}
# for i in list1:
#     dict1[i] = ' '
# list1 = list(dict1.keys())


# set1 = {'a', 'b', 'c', 'd'}
# set2 = {'e', 'a', 'f', 'd'}
# result_set = set1.intersection(set2)
# for i in set1:
#     if i in set2:
#         result_set.add(i)
# print(result_set)

# result_set.clear()
# print(result_set)

set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
# res_set34 = set3.difference(set4)
# res_set43 = set4.difference(set3)
# for i in set3:
#     if i not in set4:
#         res_set34.add(i)
# for x in set4:
#     if x not in set3:
#         res_set43.add(x)
# print(res_set34)
# print(res_set43)
