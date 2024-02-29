import tkinter as tk
import random


root = tk.Tk()
root.title('Label Widget')
root.geometry('500x300+700+300')

COLORS = [('#E53935', '#fff'), ('#4a148c', '#fff'), ('#bbdefb', 'black'), ('#ff9800', 'black')]

def get_input():
    print(text := inp.get())
    print(inp_text.get())
    label['text'] = text


def set_input():
    clear_input()
    inp.insert(0, 'New text from bot')


def clear_input():
    inp.delete(0, 'end')


btn = tk.Button(root, text='Get', font="Verdana 10 bold", width = 12, command=get_input)
btn.pack(pady=10)

btn2 = tk.Button(root, text='Set', font="Verdana 10 bold", width = 12, command=set_input)
btn2.pack(pady=10)

btn3 = tk.Button(root, text='Clear', font="Verdana 10 bold", width = 12, command=clear_input)
btn3.pack(pady=10)

s = ("""'is this maintenance?:engineers while they do usual development/integration task unless there is some substandard '
     'situations. So please next timtherwise we are '
     'losing time stretching the communication chain. Thanks.'""")

inp_text = tk.StringVar() #создали переменную класса strinvariable
inp_text.set('Placeholder') #задали ей значение переменной S


label = tk.Label(root, text='Text lablebleble', bg='#000', fg='#fff', width=15, height=4, padx=5, pady=5, font="Verdana 10 bold")
label.pack(pady=10)

inp = tk.Entry(root, textvariable=inp_text, justify='left', width=40)
# inp.insert('end', '111')  # tk.END
inp.pack(pady=10)



root.mainloop()