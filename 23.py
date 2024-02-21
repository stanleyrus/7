# code = 404
# match code:
#     case 200:
#         print(f'{code} - OK')
#     case 300 | 301 | 302:
#         print(f'{code} - Redirect')
#     case 400 | 403 | 404:
#         print(f'{code} - Client Error')
#     case _:  # fdf
#         print(f'{code} - Server Error')

# lang_orig = input('Type language (en, us, ru, de): ')
# lang = lang_orig.lower()
# match lang:
#     case 'en' | 'us' if lang == lang_orig:
#         print('Hello niga')
#     case 'en' | 'us':
#         print('HELLO')
#     case 'ru':
#         print('Привет дебил')
#     case 'de':
#         print('Hile Gitler')
#     case _:
#         print('Please choose laguage niga')

age = int(input('How old are you? '))
match age:
    case age if age < 18:
        print(f'{age} < 18')
    case age if 65 < age <= 100:
        print(f'You dont need it you have {age} years old man!')
    case age if age > 100:
        print(f'Are you sure niga? {age} years old is quiet much!')
    case _:
        print(f'{age} is OK')
