import os
import hashlib
import getpass
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Login credentials
correct_user = "admin"

correct_password = "kali123"

correct_hash = hashlib.sha256(
    correct_password.encode()
).hexdigest()

# Banner
print(Fore.CYAN + """
========================================
         JOSEPH CYBER TOOLKIT
========================================
""")

# Login
username = input(
    Fore.YELLOW + "Username: "
)

password = getpass.getpass(
    Fore.YELLOW + "Password: "
)

entered_hash = hashlib.sha256(
    password.encode()
).hexdigest()

# Verify login
if username == correct_user and entered_hash == correct_hash:

    print(Fore.GREEN + "\n[✓] ACCESS GRANTED")

    # MAIN LOOP
    while True:

        print(Fore.CYAN + """
========================================
                MENU
========================================

1. Banner Scanner
2. Fast Scanner
3. LAN Scanner
4. Advanced LAN Scanner
5. System Information
6. Website Analyzer
7. Password Tool
8. Encrypt File
9. Decrypt File
10. Integrity Checker
11. Directory Finder
12. View Log Files
13. Live Monitor
14. Log Viewer
15. Exit

========================================
""")

        choice = input(
            Fore.YELLOW + "Select Option: "
        )

        # Fast scanner
        if choice == "1":

            os.system("python3 fastscanner.py")

        # Banner scanner
        elif choice == "2":

            os.system("python3 bannerscanner.py")

        # LAN scanner
        elif choice == "3":

            os.system("python3 lanscanner.py")

        # Advanced LAN scanner
        elif choice == "4":

            os.system("python3 adv_lanscanner.py")

        # System info
        elif choice == "5":

            os.system("python3 sysinfo.py")

        # Website analyzer
        elif choice == "6":

            os.system("python3 webinfo.py")

        # Password tool
        elif choice == "7":

            os.system("python3 password_tool.py")

        # Encryptor
        elif choice == "8":

            os.system("python3 encryptor.py")

        # Decryptor
        elif choice == "9":

            os.system("python3 decryptor.py")

        # Integrity checker
        elif choice == "10":

            os.system("python3 integrity_checker.py")

        # Directory finder
        elif choice == "11":

            os.system("python3 dirfinder.py")

        # View logs
        elif choice == "12":

            os.system("ls *.txt")

            input(
                Fore.YELLOW +
                "\nPress ENTER to continue..."
            )
        #live monitor
        elif choice =="13":
            os.system("python3 monitor.py")
        #Log viewer
        elif choice =="14":
            os.system("python3 logviewer.py")
        # Exit
        elif choice == "15":
            print(Fore.RED + "\nGoodbye!")

            break

        # Invalid choice
        else:

            print(Fore.RED + "\n[!] Invalid Option")

else:

    print(Fore.RED + "\n[!] ACCESS DENIED")
