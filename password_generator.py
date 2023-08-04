import random
from colorama import Fore

# Constant Variables
LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL_SYMBOLS = "!#$%^&*()<>?'[]"

# password variables
passwd_length = 15
include_upper = True
include_numbers = True
include_symbols = True

# Main loop variable
running = True

def main():
    welcome_message = "Welcome to Password Generator\n"
    print(Fore.GREEN + welcome_message)

    help_message = f"Type {Fore.RED}'help'{Fore.GREEN} for available commands.\n"
    print(help_message)


    while running:
        command_line()

    print(Fore.RESET) # reset the terminal to normal colors

def command_line():
    global running

    user_input = input(f">>> {Fore.RED}").lower().strip()
    
    print(Fore.GREEN)

    if user_input == "exit":
        running = False
    elif user_input == "help":
        print_help()
    elif user_input == "print_default":
        print_default()
    elif user_input == "generate_password":
        generate_password()
    else:
        print(f"Command {Fore.RED}{user_input}{Fore.GREEN} not available!\n")

def print_help():
    available_commands = f"""Commands:
    {Fore.RED}exit{Fore.GREEN}: terminates the script
    {Fore.RED}generate_password{Fore.GREEN}: starts password generation prompts
    {Fore.RED}print_default{Fore.GREEN}: prints default password generation settings\n"""

    print(available_commands)

def print_default():

    default_preferences = f"""{Fore.GREEN}Default Preferences:
    Password length: {Fore.RED}{passwd_length}{Fore.GREEN}
    Include uppercase: {Fore.RED}{include_upper}{Fore.GREEN}
    Include numbers: {Fore.RED}{include_numbers}{Fore.GREEN}
    Include symbols: {Fore.RED}{include_symbols}{Fore.GREEN}\n"""

    print(default_preferences)

def generate_password():

    while True:
        try:
            choice = input(f"{Fore.GREEN}Do you want to generate password with default values? (y/n): {Fore.RED}").strip().lower()
            if choice == "y":
                print_default()
                print(f"{Fore.GREEN}Generating default password...")
                print(f"Your password is '{Fore.RED}{password_algorithm(passwd_length, include_upper, include_numbers, include_symbols)}{Fore.GREEN}'")
                break
            elif choice == "n":
                print(f"{Fore.GREEN}Your password is: {Fore.RED}{custom_password()}{Fore.GREEN}")
                break
            else:
                print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")
        except:
            print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")

def default_password(length):
    
    simple_password = ""

    for i in range(length):
        simple_password += random.choice(LOWER_CASE)

    return simple_password

def custom_password():

    while True:
        try:
            passwd_length = int(input(f"{Fore.GREEN}Enter password length: {Fore.RED}"))
            print(passwd_length)
            break
        except:
            print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")

    while True:
        try:
            user_choice  = (input(f"{Fore.GREEN}Include upper cases? (y/n): {Fore.RED}")).lower().strip()
            
            if user_choice == "y":
                include_upper = True
                print(include_upper)
                break
            elif user_choice == "n":
                include_upper = False
                print(include_upper)
                break
            else:
                print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")
        except:
            print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")

    while True:
        try:
            user_choice  = (input(f"{Fore.GREEN}Include numbers? (y/n): {Fore.RED}")).lower().strip()
            
            if user_choice == "y":
                include_numbers = True
                print(include_numbers)
                break
            elif user_choice == "n":
                include_numbers = False
                print(include_numbers)
                break
            else:
                print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")
        except:
            print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")

    while True:
        try:
            user_choice = (input(f"{Fore.GREEN}Include symbols? (y/n): {Fore.RED}")).lower().strip()
            
            if user_choice == "y":
                include_symbols = True
                print(include_symbols)
                break
            elif user_choice == "n":
                include_symbols = False
                print(include_symbols)
                break
            else:
                print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")
        except:
            print(f"{Fore.RED}ERROR{Fore.GREEN} unexpected input.")

    return password_algorithm(passwd_length, include_upper, include_numbers, include_symbols)

def password_algorithm(length, has_upper, has_numbers, has_symbols):
    
    product = ""
    simple_password = default_password(length)

    # no options were selected but the length has been specified
    if has_upper is False and has_numbers is False and has_symbols is False:
        
        product = simple_password

    # only include_upper was selected
    if has_upper is True and has_numbers is False and has_symbols is False:
        
        upper_case = length - random.choice(range(2, length))

        list_password = [character for character in simple_password]

        for character in range(upper_case):
            list_password[random.choice(range(length))] = random.choice(UPPER_CASE)

        for character in list_password:
            product += character
    
    # only include_numbers was selected
    elif has_upper is False and has_numbers is True and has_symbols is False:
        
        numbers = length - random.choice(range(2, length))

        list_password = [character for character in simple_password]

        for character in range(numbers):
            list_password[random.choice(range(length))] = random.choice(NUMBERS)

        for character in list_password:
            product += character

    # only include_symbols was selected
    elif has_upper is False and has_numbers is False and has_symbols is True:
        
        symbols = length - random.choice(range(2, length))

        list_password = [character for character in simple_password]

        for character in range(symbols):
            list_password[random.choice(range(length))] = random.choice(SPECIAL_SYMBOLS)

        for character in list_password:
            product += character

    # upper cases and numbers selected
    elif has_upper is True and has_numbers is True and has_symbols is False:
        
        upper_case = length - random.choice(range(2, length))
        numbers = length - random.choice(range(2, length))

        list_password = [character for character in simple_password]

        for character in range(upper_case):
            list_password[random.choice(range(length))] = random.choice(UPPER_CASE)

        for character in range(numbers):
            list_password[random.choice(range(length))] = random.choice(NUMBERS)

        for character in list_password:
            product += character

    # upper cases and symbols selected
    elif has_upper is True and has_numbers is False and has_symbols is True:
        
        upper_case = length - random.choice(range(2, length))
        symbols = length - random.choice(range(2, length))

        list_password = [character for character in simple_password]

        for character in range(upper_case):
            list_password[random.choice(range(length))] = random.choice(UPPER_CASE)

        for character in range(symbols):
            list_password[random.choice(range(length))] = random.choice(SPECIAL_SYMBOLS)

        for character in list_password:
            product += character

    # symbols and number selected
    elif has_upper is False and has_numbers is True and has_symbols is True:
        
        symbols = length - random.choice(range(2, length))
        numbers = length - random.choice(range(2, length))

        list_password = [character for character in simple_password]

        for character in range(symbols):
            list_password[random.choice(range(length))] = random.choice(SPECIAL_SYMBOLS)

        for character in range(numbers):
            list_password[random.choice(range(length))] = random.choice(NUMBERS)

        for character in list_password:
            product += character
    # upper cases, symbols, and numbers
    elif has_upper is True and has_numbers is True and has_symbols is True:
        
        upper_case = length - random.choice(range(1, length-1)) # added -1 because this is the first set of characters added to the password
        numbers = length - random.choice(range(1, length))      # therefore it may be overwritten by NUMBERS and SPECIAL_SYMBOLS
        symbols = length - random.choice(range(1, length))      # this way it has better odds

        list_password = [character for character in simple_password]

        for character in range(upper_case):
            list_password[random.choice(range(length))] = random.choice(UPPER_CASE)

        for character in range(numbers):
            list_password[random.choice(range(length))] = random.choice(NUMBERS)

        for character in range(symbols):
            list_password[random.choice(range(length))] = random.choice(SPECIAL_SYMBOLS)

        for character in list_password:
            product += character
    
    return product

# check if we are running as an independent file
if __name__ == '__main__':
    main()
