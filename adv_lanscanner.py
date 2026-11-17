import os
import socket
import threading
import time
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Save results file
results = open("devices.txt", "a")

# Store devices
found_devices = []

# Banner
print(Fore.CYAN + """
========================================
        ADVANCED LAN SCANNER
========================================
""")

# User input
network = input(Fore.YELLOW + "Enter network base (example 192.168.1): ")

# Start timer
start = time.time()

# Scanner function
def scan(ip):

    try:

        response = os.system(
            f"ping -c 1 -W 1 {ip} > /dev/null 2>&1"
        )

        if response == 0:

            try:

                hostname = socket.gethostbyaddr(ip)[0]

            except:

                hostname = "Unknown"

            # Display results
            print(Fore.GREEN + "\n[+] DEVICE FOUND")

            print(Fore.CYAN + f"IP ADDRESS : {ip}")

            print(Fore.YELLOW + f"HOSTNAME   : {hostname}")

            # Save results
            results.write(f"{ip} - {hostname}\n")

            # Store in memory
            found_devices.append((ip, hostname))

    except:

        pass

# Create scanning threads
for i in range(1, 255):

    ip = f"{network}.{i}"

    thread = threading.Thread(target=scan, args=(ip,))

    thread.start()

# Finish timer
end = time.time()

# Final info
print(Fore.MAGENTA + "\n[~] Network scan launched...")

print(Fore.CYAN + f"[TIME STARTED]  {start}")

print(Fore.CYAN + f"[TIME FINISHED] {end}")

# Show total devices
print(Fore.GREEN + f"\n[✓] Total Devices Found: {len(found_devices)}")

# Show summary
print(Fore.YELLOW + "\n[DEVICE SUMMARY]")

for device in found_devices:

    print(Fore.WHITE + f"-> {device[0]} | {device[1]}")

# Close results file
results.close()

print(Fore.GREEN + "\n[✓] Results saved to devices.txt")
