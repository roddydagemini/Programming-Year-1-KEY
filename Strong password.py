# Create a secure password that has at least 8 characters, a number, and a capitalized letter.

def check_password(password):
    # Check to see if the lenght of the password is at least 8 characters long
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    # Checks to make sure that the digit input is from 0 to 9. If it doesn't contain a number 
        # it gives invalid response. 
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."
    # Checks to make sure that the password has a capitzalied letter
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    # If the password meets all the requirements it will say it is secure. 
    return "Password is secure!"
secure_password = input ("Please input a secure password: ")
result = check_password(secure_password)
print(result)