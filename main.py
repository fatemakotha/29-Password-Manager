# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200, bg="white")
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image) #half of 200 is 100, so thats the center of the page
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2)

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)

login_input = Entry(width=36)
login_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entry
password_input = Entry()
password_input.grid(column=1, row=3)


generate_button = Button(text="Generate Button")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add")
add_button.grid(column=1, row=4)





#Entry
# miles_input = Entry(width=10)
# print(miles_input.get())
# miles_input.grid(column=1, row=0)
# miles_input.config(width=7)















window.mainloop()

