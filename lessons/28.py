# empty_list = []
# print(type(empty_list))
# print(empty_list)


list1 = [1, 2.4, None, [1, 2, 3, True, False], 'hello']
print(list1)


list2 = list('hello, world!')
print(list2)

list3 = list(range(1, 11))
print(list3)

print('list4')
list4 = [i for i in 'Hello, world!'[::-1]]
print(list4)

# or
print('list5')
list5 = [i for i in 'Hello world!' if i != ' ' and i != ',' and i != '!']
print(list5)

# or
print('list6')
symbols = [' ', ',', '!']
list6 = [i for i in 'Hello world!' if i not in symbols]
print(list6)

# or
print('list7')
list7 = [i.lower() * 2 for i in 'Hello world!' if i not in symbols]
print(list7)
# or
print('list8')
list8 = [(i.lower() * 2 for i in 'Hello world!' if i not in symbols),
         list(range(1, 5))]
print(list8)
