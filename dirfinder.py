import requests
import time
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Results file
results = open("dirfinder_logs.txt", "a")

# Banner
print(Fore.CYAN + """
██████╗ ██╗██████╗ ███████╗██╗███╗   ██╗██████╗
██╔══██╗██║██╔══██╗██╔════╝██║████╗  ██║██╔══██╗
██║  ██║██║██████╔╝█████╗  ██║██╔██╗ ██║██║  ██║
██║  ██║██║██╔══██╗██╔══╝  ██║██║╚██╗██║██║  ██║
██████╔╝██║██║  ██║██║     ██║██║ ╚████║██████╔╝
╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝
""")

print(Fore.GREEN + "=" * 50)
print(Fore.YELLOW + "        WEBSITE DIRECTORY FINDER")
print(Fore.YELLOW + "        Directory Finder v1.1")
print(Fore.GREEN + "         Developed by Sejoshack")
print(Fore.GREEN + "=" * 50)
# User input
target = input(
    Fore.CYAN +
    "\nEnter target URL (https://example.com): "
)

# Directories
directories = [
    "admin",
    "login",
    "dashboard",
    "uploads",
    "images",
    "backup",
    "config",
    "api",
    "robots.txt",
    "test"
]

# Start timer
start = time.time()

print(Fore.MAGENTA + "\n[~] Starting scan...\n")

# Save target
results.write("\n====================================\n")

results.write(f"TARGET : {target}\n")

try:

    for directory in directories:

        url = f"{target}/{directory}"

        try:

            response = requests.get(url)

            if response.status_code == 200:

                print(
                    Fore.GREEN +
                    f"[FOUND] {url} ({response.status_code})"
                )

                results.write(
                    f"[FOUND] {url} ({response.status_code})\n"
                )

            elif response.status_code == 403:

                print(
                    Fore.YELLOW +
                    f"[FORBIDDEN] {url} ({response.status_code})"
                )

                results.write(
                    f"[FORBIDDEN] {url} ({response.status_code})\n"
                )

            else:

                print(
                    Fore.RED +
                    f"[NOT FOUND] {url} ({response.status_code})"
                )

                results.write(
                    f"[NOT FOUND] {url} ({response.status_code})\n"
                )

        except:

            print(Fore.RED + f"[ERROR] {url}")

            results.write(f"[ERROR] {url}\n")

except Exception as e:

    print(Fore.RED + f"\n[MAIN ERROR] {e}")

    results.write(f"MAIN ERROR : {e}\n")

# Finish timer
end = time.time()

print(Fore.CYAN + f"\n[TIME STARTED] : {start}")

print(Fore.CYAN + f"[TIME FINISHED] : {end}")

# Save timing
results.write(f"\nTIME STARTED : {start}\n")

results.write(f"TIME FINISHED : {end}\n")

# Close file
results.close()

print(Fore.GREEN + "\n[✓] Results saved to dirfinder_logs.txt")

# Pause before exit
input(Fore.YELLOW + "\nPress ENTER to return to toolkit...")
