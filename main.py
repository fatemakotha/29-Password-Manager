from tkinter import * #does not install another module of tkinter which is the message box
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols +password_numbers #gives: sdf43334&*&#$%453
    random.shuffle(password_list) #shuffles sdf43334&*&#$%453 to &*&#$%453sdf43334

    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)
    password_entry.insert(0, password) #inserts the randomly generated password into the 0th index of password_entry when user clicks "generate" *
    pyperclip.copy(password) #insert the text we want to copy, which in this case is the password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0: #checks whether user left anything blank
        messagebox.showinfo(title="OOPS!", message="Please don't keep any fields empty")
    else:
        # messagebox.showinfo(title="Title", message="Mess") #shows a title and a message in popup **
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n "
                                                      f"Email: {email} \n Password: {password} \n"
                                                      f" Do you want to save?") #asks ok or cancel in pop up
                                                      #returns True or False *************
        #if user clicks Cancel, then is_ok=False
        #if user clicks Okay, then is_okay=True, then do the following code:
        if is_ok:
            with open("data.txt", "a") as data_file: #opens in append mode and creates the file names info.txt as there is no file of that name here
                data_file.write(f"{website} | {email}| {password}\n")
                website_entry.delete(0, END) #CLEARS EVERYTHING FROM 0TH INDEX TO LAST IN WEBSITE TEXTBOX
                password_entry.delete(0, END) #CLEARS EVERYTHING FROM 0TH INDEX TO LAST IN PASSWORD TEXTBOX






# ---------------------------- UI SETUP ------------------------------- #


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
generate_password_button = Button(text="Generate Button", command=generate)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

















window.mainloop()

