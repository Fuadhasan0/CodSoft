import random
import string

def get_valid_length() -> int:
    while True:
        try:
            length = int(input("Enter password length (min 6): "))
            if length < 6:
                print("Password must be at least 6 characters!")
                continue
            return length
        except ValueError:
            print("Please enter a valid number!")

def select_complexity() -> str:
    print("\nSelect complexity options:")
    return {
        'lower': input("Include lowercase letters? (y/n): ").lower() == 'y',
        'upper': input("Include uppercase letters? (y/n): ").lower() == 'y',
        'digits': input("Include numbers? (y/n): ").lower() == 'y',
        'symbols': input("Include symbols? (y/n): ").lower() == 'y'
    }

def generate_password() -> str:
    print("\n" + "="*30)
    print("PASSWORD GENERATOR")
    print("="*30)
    
    length = get_valid_length()
    complexity = select_complexity()

    char_pool = []
    if complexity['lower']: char_pool += string.ascii_lowercase
    if complexity['upper']: char_pool += string.ascii_uppercase
    if complexity['digits']: char_pool += string.digits
    if complexity['symbols']: char_pool += string.punctuation

    if not char_pool:
        print("\nError: You must enable at least one character type!")
        return ""

    password = random.choices(char_pool, k=length)
    random.shuffle(password) 
    
    return "\n✅ Your secure password: " + ''.join(password)

if __name__ == "__main__":
    result = generate_password()
    print(result)