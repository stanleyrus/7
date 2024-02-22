# import this

# def fn_outer(param):
#     def fn_inner():
#         print(param)

#     return fn_inner


# # fn_outer('TEST')()
# f = fn_outer('TEST')
# f()
# fn_outer('TEST')()

# def counter(start=0):
#     def update_counter():
#         nonlocal start
#         start += 1
#         return start

#     return update_counter


# counter1 = counter()
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())

# def fn_outer(param_outer):
#     def fn_inner(param_inner):
#         print(param_outer, param_inner)

#     return fn_inner


# fn_outer('test1')('test2')
# # OR
# f = fn_outer('nu_i_chto')
# f('hello man')
