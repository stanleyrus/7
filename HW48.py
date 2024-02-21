# list1 = ['david', 'peter', 'jenifer']
# tup1 = ('paris', 'minsk', 'mexico')


# def el_cap(lst, tpl=False):
#     if tpl:
#         return tuple(x.capitalize() for x in lst)
#     return [x.capitalize() for x in lst]


# print(el_cap(list1, tuple))


# def el_cap(lst, tpl=False):
#     data = map(lambda el: el.capitalize(), lst)
#     if tpl:
#         return tuple(data)
#     return list(data)


# print(el_cap(tup1))


# list1 = [i.capitalize() for i in list1]
# print(list1)

# tup1 = tuple([i.capitalize() for i in list(tup1)])
# print(tup1)


# def stas(x):
#     return x.capitalize()


# list1 = map(stas, list1)
# print(list(list1))


# def stas2(x, type=list):
#     print(type(map(lambda x: x.capitalize(), x)))


# stas2(list1)


# cities = [
#     ['Mexico', 8_855_000],
#     ['Paris', 2_161_000],
#     ['Minsk', 1_975_000],
#     ['Rio de Janeiro', 6_748_000],
#     ['Tokio', 13_960_000],
# ]

# dicts = dict(cities)
# print(dicts)


# best = list(filter(lambda x: dicts[x] > 2_000_000, dicts))

# print(best)

# def filter_data(lst, min_pop):
#     return [i for i in lst if i[1] > min_pop]


# print(filter_data(cities, 5_000_000))


# def filt_cit(lst, min_pop):
#     def set_filter(x):
#         return x[1] > min_pop
#     print(list(filter(set_filter, lst)))


# filt_cit(cities, 12_000_000)
# # print(cities)
# # dicts = dict(cities)
# print(dicts)


# def stan2(how):
#     listik = list(filter(lambda x: how < dicts[x], dicts))
#     print(listik)


# stan2(5000000)


d = 'a roza Upala na lapu azora'
c = 'kabala'

def cheker(y):
    y = y.lower().replace(' ', '')
    if y == y[::-1]:
        print('Yes it is')
    else:
        print('No it isnt')


cheker(d)



# def cheker(x):
#     return x == x[::-1]

# print(cheker(d.lower().replace(' ', '')))













# def chek(lst):
#     l = list(filter(lambda x: x != ' ', lst))
#     s =  .join(l)
#     n = s[::-1]

#     if s == n:
#         print(f'{s} = {n} - YES IT IS')
#     else:
#         print(f'{s} != {n} - no sorry')


# chek(c)
# chek(d)


# d = 'a roza upala na lapu Azora'
# c = 'kabala'


# def cheker(z: str) -> bool:
#     return z == z[::-1]


# print(cheker(d.lower().replace(' ', '')), )
