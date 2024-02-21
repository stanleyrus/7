# age = int(input('How much your old?  '))
# while age < 18 or age > 65:
#     print('Its a bad old niga!')
#     age = int(input('How much your old?  '))
# else:
#     print('Welcome beach!')

# age = int(input('How much your old?  '))
# while age < 18 or age > 65:
#     if age < 18:
#         print('You too young!')
#     elif 65 < age < 100:
#         print('you dont need it man!')
#     elif age > 100:
#         print('you are seriously?')
#     age = int(input('How much your old?  '))
# else:
#     print('Welcome niga')

while True:
    age = int(input('How much your old?  '))
    if age < 18:
        print('You too young!')
    elif 65 < age < 100:
        print('you dont need it man!')
    elif age > 100:
        print('you are seriously?')
    else:
        print('Welcome niga')
        break
