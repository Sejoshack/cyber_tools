import hashlib
import time
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Results file
results = open("integrity_logs.txt", "a")

# Banner
print(Fore.CYAN + """
██╗███╗   ██╗████████╗███████╗ ██████╗
██║████╗  ██║╚══██╔══╝██╔════╝██╔════╝
██║██╔██╗ ██║   ██║   █████╗  ██║
██║██║╚██╗██║   ██║   ██╔══╝  ██║
██║██║ ╚████║   ██║   ███████╗╚██████╗
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝
""")

print(Fore.GREEN + "=" * 50)
print(Fore.YELLOW + "      FILE INTEGRITY CHECKER")
print(Fore.GREEN + "=" * 50)

# User input
filename = input(
    Fore.CYAN + "\nEnter file to check: "
)

# Start timer
start = time.time()

try:

    # Read file
    with open(filename, "rb") as file:

        data = file.read()

    # Generate hashes
    md5_hash = hashlib.md5(data).hexdigest()

    sha256_hash = hashlib.sha256(data).hexdigest()

    # Display hashes
    print(Fore.GREEN + "\n[✓] HASHES GENERATED SUCCESSFULLY")

    print(Fore.MAGENTA + "\n[MD5 HASH]")

    print(Fore.YELLOW + md5_hash)

    print(Fore.MAGENTA + "\n[SHA256 HASH]")

    print(Fore.YELLOW + sha256_hash)

    # Save results
    results.write("\n====================================\n")

    results.write(f"FILE : {filename}\n")

    results.write(f"MD5 : {md5_hash}\n")

    results.write(f"SHA256 : {sha256_hash}\n")

    # Verification
    print(Fore.CYAN + "\n[INTEGRITY VERIFICATION]")

    original_hash = input(
        Fore.YELLOW +
        "Enter original SHA256 hash (or ENTER to skip): "
    )

    if original_hash:

        if original_hash == sha256_hash:

            print(Fore.GREEN + "\n[✓] FILE VERIFIED")

            results.write("STATUS : VERIFIED\n")

        else:

            print(Fore.RED + "\n[!] FILE MODIFIED")

            results.write("STATUS : MODIFIED\n")

    else:

        print(Fore.CYAN + "\n[~] Verification skipped")

        results.write("STATUS : SKIPPED\n")

except Exception as e:

    print(Fore.RED + f"\n[ERROR] {e}")

    results.write(f"ERROR : {e}\n")

# End timer
end = time.time()

# Timing
print(Fore.CYAN + f"\n[TIME STARTED] : {start}")

print(Fore.CYAN + f"[TIME FINISHED] : {end}")

results.write(f"TIME STARTED : {start}\n")

results.write(f"TIME FINISHED : {end}\n")

# Close file
results.close()

print(Fore.GREEN + "\n[✓] Results saved to integrity_logs.txt")

# Pause before exit
input(Fore.YELLOW + "\nPress ENTER to return to toolkit...")
