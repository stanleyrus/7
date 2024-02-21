

# name = 'John'
# age = 30
# print(f'30 {name=!s}, {age=}')
for y in range(1, 3):
    print(f'ON {y}')
    for i in range(2, 4):
        print(f'{y} x {i} = {y*i}\t', end='')
    print('')
else:
    print('Well done')
# y = 2
# while y <= 9:
#     print(f'ON {y} suka : ')
#     i = 2
#     while i <= 10:
#         print(f'\t{y} x {i} = {y*i}')
#         i += 1
#     y += 1


# i = 1
# while i <= 10:
#     print(f'Tablica na {i}')
#     x = 2
#     while x <= 10:
#         print(f'\t{i} X {x} = {i*x}')
#         x += 1
#     i += 1

for i in range(2, 10):
    print(f'Tablica na {i}')
    for x in range(2, 10):
        print(f'\t{i} X {x} = {i*x}')
