# def greeting(say='Hello', name='Barny'):
#     '''you shoul input 2 positional args'''
#     return f'{say}, {name} !'


# print(greeting(name='Jack'))

# print(greeting('Hi', 'John'))
# print(greeting('Stop it '))


# def greeting( name, say='Hello'):
#     return f'{say}, {name} !'


# print(greeting(name='Jack', say='Hi'))
# print(1, 2, sep='!', end='\n')


# def greeting(name, say='Hello'):
#     return f'{say}, {name} !'


# print(greeting(name='Barni'))


# def get_sum(a, b, c=1, d=0):
#     return a + b + c + d


# print(get_sum(5, 7))
# print(get_sum(5, 7, 10, 7))
# print(get_sum(5, 7, 20, c=10))


def get_sum2(x, y, *aragon, mult=2, **kuk):
    print(x)
    print(y)
    print(aragon)
    print(mult)
    print(kuk)


get_sum2(1, 2, 3, 4, 5, 6, mult=3, a=1, b=5, c=2)
# print('test', 'test2', sep='!')

# / *

# def my_func(a1, b, /, c, d, *, e, f):
#     print(a1, b, c, d, e, f)


# my_func(1, 2, c=3, d=4, e=5, f=6)
