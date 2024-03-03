def check_password_strength(password):
    has_numbers_and_letters = False
    has_special_characters = False
    special_characters = "!@#$%^&*(){}[]<>"

    for char in password:
        if char.isalnum():
            has_numbers_and_letters = True 
        elif char in special_characters:
            has_special_characters = True

    if has_special_characters and has_numbers_and_letters and len(password) >= 8:
        return "Strong Password"
    elif len(password) >= 8 and not has_special_characters:
        return "Weak Password"
    else:
        return "Invalid Password"

def main():
    password = input()
    password_strength = check_password_strength(password)
    print(password_strength)
main()