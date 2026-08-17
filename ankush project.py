 
import random
import string

def generate_password(length):
    
    letters = string.ascii_letters   
    digits = string.digits
    symbols = string.punctuation     

    
    all_characters = letters + digits + symbols

   
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


try:
    length = int(input("Enter the desired password length: "))
    if length < 6:
        print("Password length should be at least 6 characters for security.")
    else:
        strong_password = generate_password(length)
        print("\n🔐 Your Generated Password is:", strong_password)
except ValueError:
    print("Please enter a valid number.")

