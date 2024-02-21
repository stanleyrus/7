# i = 1
# while i <= 3:
#     print(f'Outer loop #{i}')
#     j = 1
#     while j <= 5:
#         print(f'\tInner loop #{i}.{j}')
#         j += 1
#     i += 1

for i in range(1, 4):
    print(f'Outer loop #{i}')
    for k in range(1, 6):
        print(f'\tInner loop #{i}.{k}')
