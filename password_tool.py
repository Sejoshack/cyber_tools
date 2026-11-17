import random
import string
import hashlib
import time
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Save results file
results = open("passwords.txt", "a")

# Banner
print(Fore.CYAN + """
========================================
      PASSWORD & HASH TOOL
========================================
""")

# Password length
length = int(input(Fore.YELLOW + "Enter password length: "))

# Character set
characters = string.ascii_letters + string.digits + string.punctuation

# Start timer
start = time.time()

# Generate password
password = "".join(random.choice(characters) for i in range(length))

# Display password
print(Fore.GREEN + f"\n[✓] GENERATED PASSWORD:\n")

print(Fore.WHITE + password)

# Generate hashes
md5_hash = hashlib.md5(password.encode()).hexdigest()

sha256_hash = hashlib.sha256(password.encode()).hexdigest()

# Show hashes
print(Fore.CYAN + "\n[MD5 HASH]")

print(Fore.YELLOW + md5_hash)

print(Fore.CYAN + "\n[SHA256 HASH]")

print(Fore.YELLOW + sha256_hash)

# Finish timer
end = time.time()

# Save results
results.write("\n====================================\n")

results.write(f"PASSWORD : {password}\n")

results.write(f"MD5 : {md5_hash}\n")

results.write(f"SHA256 : {sha256_hash}\n")

results.write(f"TIME STARTED : {start}\n")

results.write(f"TIME FINISHED : {end}\n")

# Close file
results.close()

print(Fore.GREEN + "\n[✓] Results saved to passwords.txt")
