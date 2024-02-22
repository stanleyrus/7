# def fn1():
#     print('Hello from fn1')


# def fn2(func):
#     print('Hello from fn2')
#     func()

# fn2(fn1)

# def fn1():
#     print('Hello from fn1')

# f = fn1
# f()


# def my_decorator(fn):
#     def wrapper():
#         print('Before function')
#         fn()
#         print('After function')

#     return wrapper


# @my_decorator
# def fn_test():
#     print('hello from fn_test')


# fn_test()
# f = my_decorator(fn_test)
# f()

# def decor(fn):
#     def wrapper():
#         print('before')
#         fn()
#         print('after')
    
#     return wrapper



# @decor
# def fuck():
#     print('Fuck you!!!')

# fuck()

# k = decor(fuck)

# k()



# def title_capitalize(fn):
#     def wrapper():
#         title = fn()
#         title = title.capitalize()
#         return title

#     return wrapper


# def add_dot(fn):
#     def wrapper():
#         title = fn()
#         if not title.endswith('.'):
#             title += '.'
#         return title

#     return wrapper


# @title_capitalize
# @add_dot
# def hi():
#     return 'hello man'

# print(hi())



# def capital(fnc):
#     def wrap():
#         title = str(fnc())
#         title = title.capitalize()
#         print('capital - Done')
#         print(title)
#     return wrap

# def dot_add(fnc):
#     def wrap():
#         title = fnc()
#         title += '.'
#         print('dott added!')
#         print(title)
#     return wrap


# @capital
# @dot_add
# def normal():
#      return 'hello world'


# normal()






# @add_dot
# @title_capitalize
# def fn_priv():
#     return 'hello world'

# print(fn_priv())


# def title_capitalize(fn):
#     def wrapper(*args, **kwargs):
#         title = fn(*args, **kwargs)
#         title = title.capitalize()
#         return title

#     return wrapper


# def add_dot(fn):
#     def wrapper(*args, **kwargs):
#         title = fn(*args, **kwargs)
#         if not title.endswith('.'):
#             title += '.'
#         return title

#     return wrapper


# @add_dot
# @title_capitalize
# def fn_priv(s):
#     return s



# @add_dot
# @title_capitalize
# def hi():
#     return 'hi there'

# print(fn_priv('nu i chto'))
# print(hi())


# print(fn_priv('simba!'))

# print(fn_priv('Hi test.'))

# def title_capitalize(fn):
#     def wrapper(*args, **kwargs):
#         title = fn(*args, **kwargs)
#         title = title.capitalize()
#         return title

#     return wrapper


# def end_symbol(fn):
#     def wrapper(*args, **kwargs):
#         title = fn(*args, **kwargs)
#         end_s = kwargs['end'] if 'end' in kwargs else '.'  # ternar operator
#         # if 'end' in kwargs:
#         #     end_s = kwargs['end']
#         # else:
#         #     end_s = '.'
#         if not title.endswith(end_s):
#             title += end_s
#         return title

#     return wrapper


# @end_symbol
# @title_capitalize
# def hello(s, end='.'):
#     return s + end


# @end_symbol
# @title_capitalize
# def hi():
#     return 'hi there'


# print(hello('hello, world!', end='!'))
# print(hello('Hi test'))
# print(hello('Hi test', end='?'))
# print(hi())



# def kuku(*args):
#     print(*args)


# kuku('micha', 'zhora', 123, 'kikimar')

