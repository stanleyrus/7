
# dict1 = {}
# for n in range(1, 6):
#     dict1[n] = n*n
# dict1 = {n: n * n for n in range(1, 6)}
# print(dict1)

# dict3 = {'data1': 100, 'data2': -54, 'data3': 247}
# print(sum(dict3.values()))

#  OR:

# x = 0
# for value in dict3.values():
#     x += value
# print(x)

# dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# list1 = ['x', 'y', 'b', 'd', 'e']
# for el in list1:
#     if el in dict4:
#         del dict4[el]
# print(dict4)
# for i, el in enumerate(list1):
#     if el in dict4:
#         del dict4[el]

# OR

# dict5 = {}
# for key in dict4.keys():
#     if key not in list1:
#         dict5[key] = dict4[key]
# print(dict5)

# dict4 = {}
# dict5 = {
#     'red': '#FF0000',
#     'green': '#008000',
#     'black': '#000000',
#     'white': '#FFFFF'
# }
# dict5 = {k: v for k, v in sorted(dict5.items())}
# print(dict5)

# print(dict(sorted(dict5.items())))
# list1 = sorted(dict5)
# print(list1)
# for n in list1:
#     dict4[n] = dict5[n]

# print(dict4)


# list1 = [v for v in sorted(dict6.values())]
# # print(f' minimum is - {list1[0]}, maximum is - {list1[-1]}')
dict6 = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
i = 0
for v in dict6.values():
    if i == 0:
        min_num = max_num = v
        i += 1
        continue
    if v > max_num:
        max_num = v
    if v < min_num:
        min_num = v
print(f'{min_num=} and {max_num=}')
# print(list1[0], list1[-1])
# print(max(dict6.values()))
# print(min(dict6.values()))
