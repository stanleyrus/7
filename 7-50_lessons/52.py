# import random


# x = random.randint(1, 100)
# y = int(input('give me it from 1 to 100:  '))
# z = 0
# while True:
#     while x > y or x < y:
#         if x > y:
#             z += 1
#             print(f'It should be more... try again! it was trying nr {z}')
#             y = int(input('give me it from 1 to 100:  '))

#         elif x < y:
#             z += 1
#             print(f'It should be less... try again!  it was trying nr {z}')
#             y = int(input('give me it from 1 to 100:  '))
#     else:
#         z += 1
#         print(f'Yes man, it was {y}!!!  And it was trying nr {z}')
#         m = str(input('May be you want to play again? "y/n"'))
#         if m == 'y':
#             x = random.randint(1, 100)
#             z = 0
#             y = int(input('give me it from 1 to 100:  '))
#         else:
#             print('Thank you for the game!')
#             break


# from random import randint


# num = randint(1, 100)
# cnt = 0

# while True:
#     user_num = int(
#         input('I have number from 1 to 100 - please try to guess it: '))
#     while user_num != num:
#         if num > user_num:
#             cnt += 1
#             user_num = int(input('it should be bigger try again!'))
#         elif num < user_num:
#             cnt += 1
#             user_num = int(input('it should be less try again!'))
#     else:
#         cnt += 1
#         print(f'Yes it was {user_num} and you done it by trying number {cnt}')
#         answer = str(input('May be you want to play again??  "(y/n)"  '))
#         if answer == 'y':
#             cnt = 0
#             user_num = int(
#                 input('I have number from 1 to 100 - please try to guess it: '))
#         else:
#             print('Thank you for the game it was cool !!!')
#             break


import random 

x = 0 
y = random.randint(1, 100)
z = 0

while True:
    z = int(input('Please give me number ??'))
    x += 1
    while z > y or z < y:
        if z > y:
            print('Please try again it shoul be less...')
            z = int(input('Please give me number ??'))
        else:
            print('Sorry but it should be more, try again...')
            z = int(input('Please give me number ??'))
    else:
        print(f'oh yes it is {z} and you done it in {x} tryies')
        w = input('May be try again? ')
        if w == 'y':
            y = random.randint(1, 100)
        else:
            print('thank you')
            break