import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''
    
    # Combine all selected character sets
    all_characters = lowercase + uppercase + numbers + special
    
    if not all_characters:
        raise ValueError("At least one character set must be selected")

    # Ensure the password contains at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special:
        password.append(random.choice(special))

    # Fill the remaining length with random choices from all characters
    password += random.choices(all_characters, k=length - len(password))
    
    # Shuffle the password to make it random
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    # Customize the parameters as needed
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special)
    print("Generated Password:", password)
