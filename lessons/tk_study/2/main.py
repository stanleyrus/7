import tkinter as tk
import time


root = tk.Tk()
root.title('Button Widget')
root.geometry('500x300+700+300')

def my_fn():
    print("Hello")
    if btn['width'] == 8:
        btn['width'] = 20
    else:
        btn['width'] = 8
    btn['text'] = 'Clicked' if btn['text'] == 'Press me' else'Press me'

def my_fn2(text):
    print(text)

def update_time():
    btn4['text'] = 'Time: ' + time.strftime('%H:%M:%S')

time_now = time.strftime('%H:%M:%S')

# btn = tk.Button(root, text='Press me', font=("Times New Roman", 12, "bold"))
btn = tk.Button(root, text='Press me', width = 8, command=my_fn)
btn.pack(pady=20)

btn2 = tk.Button(root, text='Button 2', width = 8, command=lambda: my_fn2('Test'))
btn2.pack(pady=10)

btn3 = tk.Button(root, text='Button 3', width = 8, command=lambda t = time.localtime(): print(time.strftime('%H:%M', t)))
btn3.pack(pady=10)

btn4 = tk.Button(root, text=f'Time: {time_now}', command=update_time)
btn4.pack(pady=10)

root.mainloop()