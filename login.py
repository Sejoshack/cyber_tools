import hashlib
import getpass
import time
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Save log file
logs = open("login_logs.txt", "a")

# Banner
print(Fore.CYAN + """
========================================
         TOOLKIT LOGIN SYSTEM
========================================
""")

# Correct username
correct_user = "admin"

# Correct password
correct_password = "kali123"

# Hash password
correct_hash = hashlib.sha256(correct_password.encode()).hexdigest()

# User input
username = input(Fore.YELLOW + "Username: ")

password = getpass.getpass(
    Fore.YELLOW + "Password: "
)

# Hash entered password
entered_hash = hashlib.sha256(password.encode()).hexdigest()

# Start time
start = time.time()

# Verify login
if username == correct_user and entered_hash == correct_hash:

    print(Fore.GREEN + "\n[✓] LOGIN SUCCESSFUL")

    logs.write("\n====================================\n")

    logs.write(f"LOGIN SUCCESS : {username}\n")

    logs.write(f"TIME : {start}\n")

else:

    print(Fore.RED + "\n[!] LOGIN FAILED")

    logs.write("\n====================================\n")

    logs.write(f"LOGIN FAILED : {username}\n")

    logs.write(f"TIME : {start}\n")

# Close logs
logs.close()

print(Fore.CYAN + "\n[✓] Logs saved to login_logs.txt")
