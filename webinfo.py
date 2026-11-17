import requests
import time
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Save results file
results = open("webinfo.txt", "a")

# Banner
print(Fore.CYAN + """
========================================
         WEBSITE ANALYZER
========================================
""")

# User input
url = input(Fore.YELLOW + "Enter Website URL: ")

# Start timer
start = time.time()

try:

    # Send request
    response = requests.get(url)

    # Status
    print(Fore.GREEN + "\n[✓] Website Reachable")

    print(Fore.CYAN + f"\n[STATUS CODE] : {response.status_code}")

    # Save status
    results.write("\n====================================\n")
    results.write(f"URL : {url}\n")
    results.write(f"STATUS CODE : {response.status_code}\n")

    # Server info
    server = response.headers.get("Server")

    print(Fore.YELLOW + f"[SERVER] : {server}")

    results.write(f"SERVER : {server}\n")

    # Content type
    content = response.headers.get("Content-Type")

    print(Fore.GREEN + f"[CONTENT TYPE] : {content}")

    results.write(f"CONTENT TYPE : {content}\n")

    # Content length
    length = response.headers.get("Content-Length")

    print(Fore.MAGENTA + f"[CONTENT LENGTH] : {length}")

    results.write(f"CONTENT LENGTH : {length}\n")

    # Show headers
    print(Fore.CYAN + "\n[HTTP HEADERS]\n")

    results.write("\n[HTTP HEADERS]\n")

    for key, value in response.headers.items():

        print(Fore.WHITE + f"{key} : {value}")

        results.write(f"{key} : {value}\n")

except Exception as e:

    print(Fore.RED + f"\n[ERROR] {e}")

    results.write(f"\nERROR : {e}\n")

# Finish timer
end = time.time()

# Time info
print(Fore.YELLOW + f"\n[TIME STARTED] : {start}")

print(Fore.YELLOW + f"[TIME FINISHED] : {end}")

# Save timing
results.write(f"\nTIME STARTED : {start}\n")
results.write(f"TIME FINISHED : {end}\n")

# Close file
results.close()

print(Fore.GREEN + "\n[✓] Results saved to webinfo.txt")
