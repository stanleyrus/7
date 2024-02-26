import tkinter as tk

root = tk.Tk()
root.title('Stanley Application')
root.iconbitmap('logo.ico')
# root.iconphoto(False, tk.PhotoImage(file='lol.png'))
root.geometry('500x300+700+300')
# root.maxsize(600, 500)
# root.resizable(False,False)

# w = 500
# h = 300
# s_w = root.winfo_screenwidth()
# s_h = root.winfo_screenheight()
# x = int((s_w / 2) - (w / 2))
# y = int((s_h / 2) - (h / 2))
# root.geometry(f'{w}x{h}+{x}+{y}')

# root.config(bg='#000000')
root['bg'] = 'silver'

root.mainloop()

