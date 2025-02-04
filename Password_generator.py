import random
import string

def generate_password(length):
    password_type = random.choice(["numbers", "letters", "mixed"])

    if password_type == "numbers":
        char_set = string.digits
    elif password_type == "letters":
        char_set = string.ascii_letters
    else:
        char_set = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(char_set) for i in range(length))
    return password, password_type


password_length = int(input("Enter the desired length of the password: "))


generated_password, password_type = generate_password(password_length)
print(f"Generated password (type: {password_type}): {generated_password}")
