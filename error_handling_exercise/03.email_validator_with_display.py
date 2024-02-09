import tkinter as tk
from tkinter import Entry
from re import findall

class NameTooShort(Exception):
    pass

class MustContainSymbol(Exception):
    pass

class InvalidDomain(Exception):
    pass

class MoreThanOneSymbol(Exception):
    pass

class InvalidName(Exception):
    pass


def validate_email(email, result_label):
    DOMAINS = ("com", "bg", "org", "net")
    MIN_NAME_SYMBOLS = 4
    pattern = "\w+"
    try:
        if email.count("@") > 1:
            raise ModuleNotFoundError("You can use only one @ symbol!")

        if "@" not in email:
            raise MustContainSymbol("Your email must contain @")

        if len(email.split("@")[0]) <= MIN_NAME_SYMBOLS:
            raise NameTooShort(f"Name length should be more than {MIN_NAME_SYMBOLS} symbols.")

        if email.split(".")[-1] not in DOMAINS:
            raise InvalidDomain("Domain must be one of the following : com, bg, org, net")

        if findall(pattern, email.split("@")[0])[0] != email.split("@")[0]:
            raise InvalidName("Name must contain only letters, digits and underscores!")
        
        result_label.config(text="Your email is valid!", fg="green")
    except (MoreThanOneSymbol, MustContainSymbol, NameTooShort, InvalidDomain, InvalidName) as e:
        result_label.config(text=str(e), fg="red")

pattern = "\w+"

def check_email():
    email = email_entry.get()
    validate_email(email, result_label)

root = tk.Tk()
root.geometry("500x250")

email_label = tk.Label(root, text="Email: ")
email_label.pack()

email_entry = Entry(root)
email_entry.pack()

check_button = tk.Button(root, text="Check Email", command=check_email)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()