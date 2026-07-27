import tkinter as tk;
import string
import random

#  --------- Fn
def save_passwords():
    with open('file.txt', 'a') as f:
        f.write(f'{website_input.get()} | {username_input.get()} | {password_input.get()}\n')
        website_input.delete(0, 'end')
        username_input.delete(0, 'end')
        password_input.delete(0, 'end')

def generate_password():
    password = ''
    password += ''.join(random.choice(string.ascii_uppercase) for x in range(5))
    password += ''.join(random.choice(string.ascii_lowercase) for x in range(5))
    password += ''.join(random.choice(string.digits) for x in range(2))
    password += ''.join(random.choice(string.punctuation) for x in range(2))
    newPass = list(password)
    random.shuffle(newPass)
    password = ''.join(newPass)
    password_input.delete(0, 'end')
    password_input.insert(0, password)

#  --------- UI
# window config
window = tk.Tk();
window.title("Password manager")
window.config(padx=50, pady=50)

# Labels
website_label = tk.Label(text='website')
username_label = tk.Label(text='username')
password_label = tk.Label(text='password')

#Inputs
website_input = tk.Entry(width=30)
username_input = tk.Entry(width=30)
password_input = tk.Entry(width=20)

#Buttons
generate_btn = tk.Button(text='generate', command=generate_password)
add_btn = tk.Button(text='add', width=27, command=save_passwords)

#Grid
website_label.grid(column=0, row=0)
username_label.grid(column=0, row=1)
password_label.grid(column=0, row=2)

website_input.grid(column=1, row=0, columnspan=2)
username_input.grid(column=1, row=1, columnspan=2)
password_input.grid(column=1, row=2)

generate_btn.grid(column=2, row=2)
add_btn.grid(column=1, row=3, columnspan=2)


window.mainloop();