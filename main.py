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
canvas.pack()

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)







#Entry
# miles_input = Entry(width=10)
# print(miles_input.get())
# miles_input.grid(column=1, row=0)
# miles_input.config(width=7)















window.mainloop()

