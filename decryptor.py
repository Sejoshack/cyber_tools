from cryptography.fernet import Fernet
from colorama import Fore, init
import time

# Initialize colors
init(autoreset=True)

# Save logs
logs = open("decryption_logs.txt", "a")

# Banner
print(Fore.CYAN + """
========================================
         FILE DECRYPTION TOOL
========================================
""")

# Load key
with open("secret.key", "rb") as key_file:

    key = key_file.read()

cipher = Fernet(key)

# User input
filename = input(
    Fore.YELLOW + "Enter encrypted file: "
)

# Start time
start = time.time()

try:

    # Read encrypted file
    with open(filename, "rb") as file:

        encrypted_data = file.read()

    # Decrypt data
    decrypted_data = cipher.decrypt(
        encrypted_data
    )

    # Output file
    output_file = "decrypted_" + filename.replace(
        ".encrypted", ""
    )

    # Save decrypted file
    with open(output_file, "wb") as file:

        file.write(decrypted_data)

    # Success
    print(
        Fore.GREEN +
        "\n[✓] File decrypted successfully"
    )

    print(
        Fore.CYAN +
        f"[OUTPUT FILE] : {output_file}"
    )

    # Save logs
    logs.write("\n====================================\n")

    logs.write(f"FILE : {filename}\n")

    logs.write(f"OUTPUT : {output_file}\n")

    logs.write(f"TIME : {start}\n")

except Exception as e:

    print(Fore.RED + f"\n[ERROR] {e}")

    logs.write(f"\nERROR : {e}\n")

# Close logs
logs.close()

print(
    Fore.GREEN +
    "\n[✓] Logs saved to decryption_logs.txt"
)
