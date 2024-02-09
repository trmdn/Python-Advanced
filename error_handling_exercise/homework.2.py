import re


class NameTooShortError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_SYMBOLS_COUNT = 4
MAX_NAME_SYMBOLS_COUNT = 39

pattern_name = re.compile(r'^\w+$')

while True:
    email = input()
    if email == "End":
        break

    if email.count("@") > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @ symbol!")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")

    name_part = email.split("@")[0]
    if len(name_part) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters!")

    if len(name_part) >= MAX_NAME_SYMBOLS_COUNT:
        raise NameTooLongError("Name is too long")


    if email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")

    if not pattern_name.fullmatch(name_part):
        raise InvalidNameError("Name must contain only letters, digits, and underscores!")

    print("Email is valid")

