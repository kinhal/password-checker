import re
from colorama import Fore, Style

def check_password_strength(password):
    length = len(password)
    if length < 8:
        return Fore.RED + "Weak: password must be at least 8 characters long." + Style.RESET_ALL

    score = 0

    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 4 and length >= 12:
        return Fore.GREEN + "Very strong" + Style.RESET_ALL
    elif score >= 3:
        return Fore.MAGENTA + "Strong" + Style.RESET_ALL
    elif score == 2:
        return Fore.YELLOW + "Medium" + Style.RESET_ALL
    else:
        return Fore.RED + "Weak" + Style.RESET_ALL

def main():
    pwd = input(Fore.GREEN + "Enter the password to check: " + Style.RESET_ALL)
    result = check_password_strength(pwd)
    print(Fore.GREEN + f"Assessment: {result}" + Style.RESET_ALL)
    input(Fore.GREEN + "\nPress any key to exit..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
