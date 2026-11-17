from cryptography.fernet import Fernet
from colorama import Fore, init
import time

# Initialize colors
init(autoreset=True)

# Save logs
logs = open("encryption_logs.txt", "a")

# Banner
print(Fore.CYAN + """
========================================
         FILE ENCRYPTION TOOL
========================================
""")

# Generate encryption key
key = Fernet.generate_key()

# Save key
with open("secret.key", "wb") as key_file:

    key_file.write(key)

# Load key
cipher = Fernet(key)

# User input
filename = input(
    Fore.YELLOW + "Enter file to encrypt: "
)

# Start time
start = time.time()

try:

    # Read file
    with open(filename, "rb") as file:

        data = file.read()

    # Encrypt data
    encrypted_data = cipher.encrypt(data)

    # Save encrypted file
    encrypted_file = filename + ".encrypted"

    with open(encrypted_file, "wb") as file:

        file.write(encrypted_data)

    # Success message
    print(
        Fore.GREEN +
        f"\n[✓] File encrypted successfully"
    )

    print(
        Fore.CYAN +
        f"[ENCRYPTED FILE] : {encrypted_file}"
    )

    print(
        Fore.YELLOW +
        "[KEY FILE] : secret.key"
    )

    # Save logs
    logs.write("\n====================================\n")

    logs.write(f"FILE : {filename}\n")

    logs.write(f"ENCRYPTED : {encrypted_file}\n")

    logs.write(f"TIME : {start}\n")

except Exception as e:

    print(Fore.RED + f"\n[ERROR] {e}")

    logs.write(f"\nERROR : {e}\n")

# Close logs
logs.close()

print(
    Fore.GREEN +
    "\n[✓] Logs saved to encryption_logs.txt"
)
