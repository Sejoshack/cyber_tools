import socket

print("=" * 27)
print("      ADVANCED PORT SCANNER")
print("=" * 27)

target = input("Enter target IP: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

open_ports = []

print("\nScanning...\n")

for port in range(start_port, end_port + 1):

    s = socket.socket()

    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} OPEN")
        open_ports.append(port)

    s.close()

print("\nScan Complete!")

print(f"\nTotal Open Ports: {len(open_ports)}")

print("Open Ports List:")

for p in open_ports:
    print(f"-> {p}")
