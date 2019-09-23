# Local imports
from valid_password_checker import password_checker

def password_prompt():
    """Prompts the user for a password input and uses a helper function
    to determine if the password is a strong and valid one."""

    print("Welcome to the password checker prompt!")
    print("Here are the rules for a strong password:")
    print("1) contains at least 8 characters,")
    print("2) contains at least one numerical and one alphabetical character,")
    print("3) contains at least one special character, (e.g. @, #, %, *),")
    print("4) cannot contain the same character more than twice consecutively,")
    print("5) should not have patterns with increasing values of length 3 "
          + "or more (e.g. 'abc', '1234'),")
    print("6) should have the number of unique characters be greater than half"
          + " the length of the itself" )
    print("   (e.g. 'abcabcabc' fails since only "
          + " 3 unique chars < 8 length of password).")

    while True:
        password = input("\nEnter a password: ")
        if password_checker(password):
            print("Password accepted!")
            break
        else:
            print("Password not strong enough, try again!")

password_prompt()
