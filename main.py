# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as data_file: #opens in append mode and creates the file names info.txt as there is no file of that name here
        data_file.write(f"{website} | {email}| {password}\n")






# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

#____________________________________________________________________________________________________________________________________________
canvas = Canvas(width=200, height=200, bg="white")
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image) #half of 200 is 100, so thats the center of the page
canvas.grid(column=1, row=0)
#____________________________________________________________________________________________________________________________________________

#Labels:
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
#_________________________________________________________________________________________________________________________________________________________________

#Entries
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() #gets the cursor blinking in this box for user to type


email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "fatema.alam.kotha@gmail.com") #sets pre text to the 0th index
# email_entry.insert(END, "fatema.alam.kotha@gmail.com") #sets the cursor at the end to continue typing after fatema.alam.kotha@gmail.comGRDFRGHFDKGH


password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

#_________________________________________________________________________________________________________________________________________________________________

#Buttons
generate_password_button = Button(text="Generate Button")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

















window.mainloop()

