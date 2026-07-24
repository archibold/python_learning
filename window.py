import tkinter as tk

window = tk.Tk()
window.title("mile to km")

tk.Label(window, text='Mile').grid(column=0, row=0)
tk.Label(window, text='Kilometers').grid(column=0, row=1)

entry = tk.Entry(window,)

entry.grid(column=1, row=0)

def chnageEntry(value):
    print(value)

entry.bind('<KeyRelease>', chnageEntry)

window.mainloop()