import tkinter as tk



root = tk.Tk()
root.title('Pack')
root.geometry('500x300+700+300')

frame1 = tk.Frame(root)
frame1.pack(fill='x')
frame2 = tk.Frame(root)
frame2.pack(fill='both', side='bottom')

tk.Label(frame1, text='1', bg='#e53935', fg='#fff', width=8, height=4).pack(side='left')
tk.Label(frame1, text='2', bg='#8e24aa', fg='#fff', width=8, height=4).pack(side='right')
tk.Label(frame2, text='3', bg='#1e88e5', fg='#fff', width=8, height=4).pack(side='left')
tk.Label(frame2, text='4', bg='#00897b', fg='#fff', width=8, height=4).pack(side='right')

root.mainloop()