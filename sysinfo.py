import os
import socket
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

print(Fore.CYAN + """
========================================
         SYSTEM INFORMATION
========================================
""")

# Hostname
hostname = socket.gethostname()

# IP Address
try:

    ip = socket.gethostbyname(hostname)

except:

    ip = "Unknown"

# Display info
print(Fore.GREEN + f"[HOSTNAME] : {hostname}")

print(Fore.YELLOW + f"[IP ADDRESS] : {ip}")

# Linux system commands
print(Fore.CYAN + "\n[KERNEL INFO]")

os.system("uname -a")

print(Fore.CYAN + "\n[CURRENT USER]")

os.system("whoami")

print(Fore.CYAN + "\n[UPTIME]")

os.system("uptime")

print(Fore.CYAN + "\n[MEMORY USAGE]")

os.system("free -h")

print(Fore.CYAN + "\n[DISK USAGE]")

os.system("df -h")
