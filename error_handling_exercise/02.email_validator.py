from re import findall

class NameTooShort(Exception):
    pass

class MustContainSymbol(Exception):
    pass

class InvalidDomain(Exception):
    pass

class MoreThanOneSymbol(Exception):
    pass

class InvalideName(Exception):
    pass

def validate_email(email):
    DOMAINS = ("com", "bg", "org", "net")
    MIN_NAME_SYMBOLS = 4
    pattern = "\w+"

    while True:
        
        if email.count("@") > 1:
            raise ModuleNotFoundError("You can use only one @ symbol!")
        
        if "@" not in email:
            raise MustContainSymbol("Your email must contain @")
        
        if len(email.split("@")[0]) <= MIN_NAME_SYMBOLS:
            raise NameTooShort(f"Name length should be more than {MIN_NAME_SYMBOLS} symbols.")
        
        if email.split(".")[-1] not in DOMAINS:
            raise InvalidDomain("Domain must be one of the following : com, bg, org, net")
        
        if findall(pattern, email.split("@")[0])[0] != email.split("@")[0]:
            raise InvalideName("Name must contain only letters, digits and underscores!")
        
        print("Your email is valid!")

        email = input()

if __name__ == "__main__":
    email_input = input("Enter your email: ")
    validate_email(email_input)