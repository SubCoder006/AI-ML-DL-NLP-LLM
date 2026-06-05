def password_strength(password):
    if(len(password) < 8):
        print("Password is too weak.")
    elif not (any(char.isupper() for char in password) and 
            any(char.islower() for char in password) and 
            any(char.isdigit() for char in password) and 
            any(char in "!@#$%^&*~/|+-" for char in password)):
        print("Password is weak.")
    else:
        print("Password is strong.")

password_strength("subayan")
password_strength("Suba12345")
password_strength("Sub@147+gh")