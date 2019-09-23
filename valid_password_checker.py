# Standard library imports
import re


def password_checker(password):
    """Returns a boolean indicating if the passed password string
    fulfills the required criteria."""

    # Password should contain at least 8 characters
    if len(password)<8:
        print("Doesn't contain at least 8 characters!")
        return False

    # Password should contain at least one alphabetical character
    if not re.search('[a-zA-Z]', password):
        print("Doesn't contain at least one alphabetical character!")
        return False

    # Password should contain at least one numerical character
    if not re.search('[0-9]', password):
        print("Doesn't contain at least one numerical character!")
        return False

    # Password should contain one special character
    if password.isalnum():
        print("Doesn't contain at least one special character!")
        return False

    # Password shouldn't contain same char more than twice consecutively
    for x in range(len(password)-2):
        if ((password[x] == password[x+1]) and (password[x] == password[x+2])):
            print("Contains same char for more than twice consecutively: "
                  + password[x] + "!")
            return False

    # Password shouldn't have patterns of increasing values of length 3
    # or more, e.g. "abc", "1234"
    for x in range(len(password)-2):
        if ((ord(password[x]) == ord(password[x+1])-1)
            and (ord(password[x+1]) == ord(password[x+2])-1)):
            print("Contains a pattern of increasing values of length 3 or more"
                  + ": " + password[x] + password[x+1] + password[x+2] + "!")
            return False

    # Password should have the number of unique characters greater
    # than or equal to half its length
    unique_chars = set()
    for x in range(len(password)):
        unique_chars.add(password[x])
    if len(unique_chars) < len(password)/2:
        print("Number of unique characters is " + str(len(unique_chars))
               + ", which is less than half the length of the password, "
               + str(len(password)) + "/2!")
        return False

    return True
