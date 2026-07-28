import tkinter as tk
import pandas
import random

window = tk.Tk()

window.title('flash cards')
window.config(padx=50, pady=50)

#  ----- FN
list = pandas.read_csv('french_words.csv').to_dict(orient='records')
firstword =random.choice(list)

def show():
    
    # fword  =random.choice(list)
    lang.config(text='French')
    word.config(text=firstword['French'])
    show_btn.grid_forget()
    next_btn.grid(column=1)
    

def next():
    global firstword
    lang.config(text='English')
    firstword = random.choice(list)
    word.config(text=firstword['English'])
    show_btn.grid(column=1)
    next_btn.grid_forget()

#  items
lang = tk.Label(text='English', font=('Helvetica', 24, 'italic'))
word = tk.Label(text=firstword['English'], font=('Helvetica', 24, 'bold'))
show_btn = tk.Button(text='show', command=show)
next_btn = tk.Button(text='next', command=next)

# UI

lang.grid(column=1, row=0)
word.grid(column=1, row=1)
show_btn.grid(column=1)
next_btn.grid(column=1)
next_btn.grid_forget()

window.mainloop()