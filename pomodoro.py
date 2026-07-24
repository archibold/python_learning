import tkinter as tk
import math

FONTNAME = 'Helvetica'
clock_state = False
reps= 1

def counter(seconds):
    global reps
    # print(seconds)

    if seconds > 0 and clock_state:
        t_sec = f'{seconds % 60}' if seconds % 60 > 9 else f'0{seconds % 60}'
        t_min = f'{math.floor(seconds / 60)}' if math.floor(seconds / 60) > 10 else f'0{math.floor(seconds / 60)}'
        clock.config(text=f'{t_min}:{t_sec}')
        window.after(1000, counter, seconds - 1)
    elif clock_state:
        clock.config(text='00:00')
        reps += 1
        if reps % 2 == 0:
            start_break(20 if reps%10 == 0 else 5)
        else:
            start_work()
        # reset_pomodoro()


def start_work():
    clock.config(text='25:00')
    title.config(text='Work');
    window.after(1000, counter, 25*60)

def start_pomodoro():
    global clock_state
    clock_state= True
    start_button.config(state='disabled')
    reset_button.config(state='normal')
    start_work()

def start_break(minutes):
    title.config(text='Break');
    window.after(1000, counter, minutes*60)

def reset_pomodoro():
    global reps
    global clock_state 
    clock_state= False
    reps = 1
    clock.config(text='00:00')
    reset_button.config(state='disabled')
    start_button.config(state='normal')
    title.config(text='Pomodoro');

window = tk.Tk();

window.title('Pomodoro');
window.geometry('400x250')
window.config(padx=50, pady=50)

title = tk.Label(text='Pomodoro', font=(FONTNAME, 32, 'bold'))
sub = tk.Label(text='----------------',font=(FONTNAME, 32, 'bold')).grid(column=1, row=1)
title.grid(column=1, row=0)
# title
clock = tk.Label(text='00:00', font=(FONTNAME, 24), fg='yellow')
clock.grid(column=1, row=2)

start_button = tk.Button(text='start', command=start_pomodoro)
start_button.grid(column=0, row=3)
reset_button = tk.Button(text='reset', command=reset_pomodoro)
reset_button.grid(column=3, row=3)

reset_button.config(state='disabled')

window.mainloop();