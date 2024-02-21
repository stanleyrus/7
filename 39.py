# tuple1 = ()
# print(tuple1, type(tuple1))

# tuple2 = tuple()

# tuple1 = ('black', 'white', 'blue', 'orange')
# print(tuple1, type(tuple1), id(tuple1))


# tuple2 = tuple(('red', 'green', 'white'))
# print(tuple2, type(tuple2), id(tuple2))

# print(len(tuple1))
# print(tuple1[-1])
# print(tuple1[len(tuple1) - 1])
# print(tuple1[1:3])

# if 'white' in tuple1:
#     print('OK')

# print(tuple1)
# list1 = list(tuple1)
# list1[0] = 'yellow'
# list1.append('niga')
# print(list1)
# tuple1 = tuple(list1)
# print(tuple1)

# tuple1 += tuple2
# # tuple1 += (1, 2, 3)
# print(tuple1)


# # LOOP
# for i in tuple1:
#     print(i, end=' ')
# print(' ')

# for i in range(len(tuple1)):
#     print(tuple1[i], end=' ')

# print(' ')

# print(tuple2)
# tuple2 *= 2
# print(tuple2)

# x = 'good', 'year'
# print(x, type(x))

# a = (1, 2, [4, 5, 6], 3)
# print(a)
# a[2][0] = 'test'
# print(a)

# a = (1, 2, 3)
# b = [1, 2, 3]
# print(dir([]))
# print(dir(()))

# print(a.__sizeof__())
# print(b.__sizeof__())

a = 1
b = 2
a, b = b, a
print(a, b)
