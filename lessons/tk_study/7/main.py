import tkinter as tk


root = tk.Tk()
root.title('Place')
root.geometry('500x300+700+300')

#
# tk.Label(root, text='Hello, World!', padx=20, pady=10, bg='#37474f', fg='#fff', font=12).place(x=0, y=0, anchor='nw')

# tk.Entry(root).place(x=10, y=10, width=250, height=40)
# tk.Button(root, text='Send').place(x=270, y=10, width=100, height=40)
#
# tk.Entry(root).place(x=10, y=60, width=250, height=40)
# tk.Button(root, text='Send 2').place(x=270, y=60, width=100, height=40)

# tk.Label(root, text='Hello, World!', padx=20, pady=10, bg='#37474f', fg='#fff', font=12).place(x=0, y=0, anchor='nw')
# tk.Label(root, text='Hello, World!', padx=20, pady=10, bg='#37474f', fg='#fff', font=12).place(relx=1, rely=0, anchor='ne')
# tk.Label(root, text='Hello, World!', padx=20, pady=10, bg='#37474f', fg='#fff', font=12).place(relx=0, rely=1, anchor='sw')
# tk.Label(root, text='Hello, World!', padx=20, pady=10, bg='#37474f', fg='#fff', font=12).place(relx=1, rely=1, anchor='se')
# tk.Label(root, text='Hello, Stas!', padx=20, pady=10, bg='white', fg='black', font=12).place(relx=0.5, rely=0.5, anchor='center')

f1 = tk.Frame(root, bg='black')
f1.place(relwidth=0.9, relheight=0.1, relx=0.5, rely=0.05, anchor='center')
tk.Entry(f1).place(relwidth=0.7, relheight=0.9, rely=0.05, relx=0.01, anchor='nw')
tk.Button(f1, text='Send').place(relwidth=0.27, relheight=0.9, rely=0.05, relx=0.72, anchor='nw')


root.mainloop()