# # scope
# a = 'global'


# def fn():
#     # a += '!' error
#     # global a
#     a = 'local a'
#     a += '!'
#     print(a)


# print(a)
# fn()
# print(a)


# def fn2():
#     b = 'local fn2'
#     print(b)


# fn2()


# print(b)


get_double2 = lambda x: x ** 2

print(get_double2(5))


# lambda args [,...]: stmt

# def get_double2(x): return x ** 2




# print(get_double2(5))


# def max_num(x, y):
#     return x if x > y else y


max_num2 = lambda x, y: x if x > y else y


print(max_num2(4, 9))




# print(max_num(7, 5))


# def max_num2(x, y): return x if x > y else y


# print(max_num2(5, 10))


# print((lambda x, y: x if x > y else y)(40, 50))
# res = (lambda x, y: x if x > y else y)(7, 14)
# # print(res)
# print((lambda *args: args)(1, 2, 3))
