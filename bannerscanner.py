import socket
import threading
import time
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Store open ports
open_ports = []

# Save results
results = open("results.txt", "a")

# Banner
print(Fore.CYAN + """
███████╗ █████╗ ███████╗████████╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝
█████╗  ███████║███████╗   ██║
██╔══╝  ██╔══██║╚════██║   ██║
██║     ██║  ██║███████║   ██║
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝
""")

print(Fore.GREEN + "=" * 50)
print(Fore.YELLOW + "       ADVANCED FAST SCANNER")
print(Fore.GREEN + "=" * 50)

# User input
target = input(Fore.CYAN + "Enter Target IP: ")

# Timer start
start = time.time()

# Scan function
def scan(port):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:

            print(Fore.GREEN + f"\n[+] PORT {port} OPEN")

            open_ports.append(port)

            results.write(f"\n[+] PORT {port} OPEN\n")

            # Try banner grabbing
            try:

                banner = s.recv(1024).decode().strip()

                if banner:

                    print(Fore.CYAN + f"[BANNER] {banner}")

                    results.write(f"[BANNER] {banner}\n")

                else:

                    print(Fore.RED + "[!] Empty banner")

                    results.write("[!] Empty banner\n")

            except:

                print(Fore.RED + "[!] No banner received")

                results.write("[!] No banner received\n")

        s.close()

    except:

        pass

# Create threads
for port in range(1, 101):

    thread = threading.Thread(target=scan, args=(port,))

    thread.start()

# Timer end
end = time.time()

# Final info
print(Fore.YELLOW + "\n[~] Scan launched successfully...")

print(Fore.CYAN + f"[TIME STARTED] {start}")

print(Fore.CYAN + f"[TIME FINISHED] {end}")

# Show open ports
print(Fore.GREEN + "\n[OPEN PORTS FOUND]")

for p in open_ports:

    print(Fore.YELLOW + f"-> {p}")

# Close file
results.close()

print(Fore.GREEN + "\n[✓] Results saved to results.txt")
