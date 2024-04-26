import funcsss as f
import config
import datetime

print('*' * 70)
print(("""* Hi! I'll help you to know weater in every city of the world.
* Just enter request in format: city[,country_code]
* If you want to exit from program, then just press Enter"""))
print('*' * 70)

while True:
    q = input('Please enter the name of the city: ')
    if not q:
        exit('See you later :)')
    else:
        weather = f.get_weather(q)
        print("+" * 50)
        f.print_weather(weather)
        f.save_excel(weather)


