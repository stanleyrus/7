import tkinter as tk
import random


root = tk.Tk()
root.title('Label Widget')
root.geometry('500x300+700+300')

COLORS = [('#E53935', '#fff'), ('#4a148c', '#fff'), ('#bbdefb', 'black'), ('#ff9800', 'black')]

def get_label():
    print(label.cget('text')) # метод что бы получить содержание параметра элемента lable
    print(label_text.get()) # метод что бы получить содержание элемента lable_text


def set_label():
    label_text.set('go home, yanki!!!')


def change_label_color():
    index = random.randint(0, 3)
    color = COLORS[index]
    label['bg'] = color[0]
    label['fg'] = color[1]


btn = tk.Button(root, text='Get', font="Verdana 10 bold", width = 12, command=get_label)
btn.pack(pady=10)

btn2 = tk.Button(root, text='Set', font="Verdana 10 bold", width = 12, command=set_label)
btn2.pack(pady=10)

btn3 = tk.Button(root, text='Change color', font="Verdana 10 bold", width = 12, command=change_label_color)
btn3.pack(pady=10)

s = ("""'is this maintenance?:engineers while they do usual development/integration task unless there is some substandard '
     'situations. So please next timtherwise we are '
     'losing time stretching the communication chain. Thanks.'""")

label_text = tk.StringVar() #создали переменную класса strinvariable
label_text.set(s) #задали ей значение переменной S


label = tk.Label(root, textvariable=label_text, bg='#000', fg='#fff', width=50, height=4, wraplength=800, padx=5, pady=5, font="Verdana 10 bold", anchor='nw', justify='left', cursor='watch')
label.pack(pady=10)


root.mainloop()