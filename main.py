BG_COLOR="#000C1D"
BLUE="#a8d8ea"
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip

def password_creation():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list=[choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list +=[choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    entrypass.delete(0,END)
    entrypass.insert(0,password)
    pyperclip.copy(password)

def add_data():
    website=entry.get()
    username=entryemail.get()
    password=entrypass.get()
    if username=="" or website=="" or password=="":
        messagebox.showinfo("Empty Warning","You have a empty field. Please fill it up")
    else:

        its_okay=messagebox.askokcancel(title=website,message=f"These are the details entered:\nWebsite: {website}"
                                                              f"\nEmail: {username}"
                                                     f"\nPassword: {password}")
        if its_okay:
            total=website+","+username+","+password
            with open("passwordsaver.txt","a") as file:
                file.write(total+"\n")
                entry.delete(0,END)
                entrypass.delete(0,END)

# ----------------------------------------UI------------------------------------------------
window=Tk()
window.config(pady=40,padx=80,bg=BG_COLOR)
window.title("Password Generator")
canvas=Canvas(width=500,height=500,highlightthickness=0)
img_data=PhotoImage(file="passwordcreator.png")
canvas.create_image(250,250,image=img_data)
canvas.grid(column=1,row=2)
label=Label(text="Password Generator",fg=BLUE,font=("Britannic Bold",30),bg=BG_COLOR)
label.grid(column=1,row=0)

label_website=Label(text="Website:")
label_website.config(width=10,font=("Times New Roman",15),bg=BG_COLOR,fg=BLUE)
label_website.grid(row=3,column=0)

entry=Entry(width=105)
entry.grid(column=1,columnspan=2,row=3)
entry.focus()

label_email=Label(text="Email/Username:")
label_email.config(width=15,font=("Times New Roman",15),bg=BG_COLOR,fg=BLUE)
label_email.grid(row=4,column=0)

entryemail=Entry(width=105)
entryemail.grid(column=1,columnspan=2,row=4)
entryemail.insert(0,"eunnathi@gmail.com")

label_pass=Label(text="Password:")
label_pass.config(width=15,font=("Times New Roman",15),bg=BG_COLOR,fg=BLUE)
label_pass.grid(row=5,column=0)

entrypass=Entry(width=84)
entrypass.grid(column=1,row=5)

button_generate=Button(text="Generate Password",command=password_creation,width=16,bg=BLUE)
button_generate.grid(column=2,row=5)

button_add=Button(text="Add",width=20,command=add_data,bg=BLUE)
button_add.grid(column=1,row=6)

window.mainloop()