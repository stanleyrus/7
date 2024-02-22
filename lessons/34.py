# x = 10
# print(f'{x=}, {id(x)=}')
# x += 1
# print(f'{x=}, {id(x)=}')

# s = 'hello'
# print(f'{s=}, {id(s)=}')
# s += ', world'
# print(f'{s=}, {id(s)=}')

# l = [1, 2, 3]
# print(f'{l=}, {id(l)=}')
# l.append('hello')
# print(f'{l=}, {id(l)=}')


# a = b = 5
# print(f'{a=}, {id(a)=}')
# print(f'{b=}, {id(b)=}')

# a = 7
# print(f'{a=}, {id(a)=}')
# print(f'{b=}, {id(b)=}')

# import copy
# l1 = [1, 2, 3, [4, 5]]
# print(f'{l1=}, {id(l1)=}')
# l2 = l1.copy()
# import copy
# l1 = [1, 2, 3, [4, 5]]
# l2 = copy.deepcopy(l1)
# print(f'{l1=}, {id(l1)=}')
# print(f'{l2=}, {id(l2)=}')
# print(f'{l1=}, {id(l1[3])=}')
# print(f'{l2=}, {id(l2[3])=}')

l1 = [1, 2, 3]
print(f'{l1=}, {id(l1)=}')
# l1 = l1 + [4, 5]
l1 = l1.__iadd__([4, 5])
print(f'{l1=}, {id(l1)=}')

# print(dir([]))
# print(help([].__add__))
# print(help([].__iadd__))
