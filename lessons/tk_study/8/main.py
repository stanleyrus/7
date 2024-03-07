import tkinter as tk


root = tk.Tk()
root.title('Text')
root.geometry('500x300+700+300')

menu_frame = tk.Frame(root, bg='#37474f')
menu_frame.pack(fill='x')

content_frame = tk.Frame(root, bg='#78909c')
content_frame.pack(fill='both')


def add_content():
    pass

def clear_content():
    pass

def get_content():
    pass




tk.Button(menu_frame, text='Add', pady=5, command=add_content).grid(row=0, column=0, sticky='we', padx=5, pady=5)
tk.Button(menu_frame, text='Clear', pady=5, command=clear_content).grid(row=0, column=1, sticky='we', padx=5, pady=5)
tk.Button(menu_frame, text='Get', pady=5, command=get_content).grid(row=0, column=2, sticky='we', padx=5, pady=5)
# menu_frame.grid_columnconfigure(0, weight=2)
# menu_frame.grid_columnconfigure(1, weight=1)
# menu_frame.grid_columnconfigure(2, weight=0)
menu_frame.grid_columnconfigure('all', weight=2)


root.mainloop()