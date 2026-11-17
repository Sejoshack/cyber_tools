import os
import threading

print("""
====================================
        LAN DEVICE SCANNER
====================================
""")

network = input("Enter network base (example 192.168.1): ")

# Scanner function
def scan(ip):

    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

    if response == 0:

        print(f"[+] Device Found: {ip}")

# Create threads
for i in range(1, 255):

    ip = f"{network}.{i}"

    thread = threading.Thread(target=scan, args=(ip,))

    thread.start()
