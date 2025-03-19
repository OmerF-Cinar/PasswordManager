from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [(random.choice(letters)) for letter in range(random.randint(8,10))]

    pass_numbers = [(random.choice(numbers)) for number in range(random.randint(2,4))]

    pass_symbols = [(random.choice(symbols)) for symbol in range(random.randint(2,4))]

    password_list = pass_letters + pass_numbers + pass_symbols

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_value = website_entry.get()
    username_value = username_entry.get()
    password_value = password_entry.get()
    new_data = {
        website_value : {
            "email": username_value,
            "password": password_value
        }
    }

    if len(website_value) == 0 or len(password_value) == 0 or len(username_value) == 0:
        messagebox.showwarning(title="Warning", message="Don't leave required fields empty!")
    else:

        try:

            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:

            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file)

        else:
            # Updating the old data
            data.update(new_data)


            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search_password():

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website = website_entry.get()
            messagebox.showinfo(title=website, message=f"Email:{data[website]['email']}\nPassword:{data[website]['password']}")

    except KeyError:
        messagebox.showerror(title="Error", message="Data not found.")

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50, bg="white")

#Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
mypass = PhotoImage(file="logo.png")
canvas.create_image(100,100 ,image=mypass)
canvas.grid(column=1, row=0)

#Label
website_text = Label(text="Website", font=16, bg="white")
website_text.grid(column=0, row=1)

username_text = Label(text="Email/Username", font=16, bg="white")
username_text.grid(column=0, row=2)

password_text = Label(text="Password", font=16, bg="white")
password_text.grid(column=0, row=3)

#Entry

website_entry = Entry(width=22)
website_entry.grid(column=1, row=1, sticky="e")
website_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
username_entry.insert(0, "test@mail.com")

password_entry = Entry(width=22)
password_entry.grid(column=1, row=3, sticky="e")

#Button

generate_password = Button(text="Generate A Password", bg="white", width=16, command=generate_password)
generate_password.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=38, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

search_website = Button(text="Search", bg="white", width=16, command=search_password)
search_website.grid(column=2, row=1, sticky="w")

root.mainloop()
