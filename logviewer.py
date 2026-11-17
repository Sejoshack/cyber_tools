import os
from colorama import Fore, init

init(autoreset=True)

print(Fore.CYAN + """
========================================
            LOG VIEWER
========================================
""")

logs = [
    "results.txt",
    "devices.txt",
    "webinfo.txt",
    "dirfinder_logs.txt",
    "integrity_logs.txt",
    "monitor_logs.txt",
    "passwords.txt",
    "encryption_logs.txt",
    "decryption_logs.txt"
]

print(Fore.YELLOW + "\nAvailable Logs:\n")

for i, log in enumerate(logs, start=1):
    print(f"{i}. {log}")

choice = input(
    Fore.CYAN +
    "\nSelect log number: "
)

try:

    logfile = logs[int(choice)-1]

    print(
        Fore.GREEN +
        f"\nOpening {logfile}...\n"
    )

    if os.path.exists(logfile):

        with open(logfile, "r") as file:

            print(file.read())

    else:

        print(
            Fore.RED +
            "\nLog file does not exist."
        )

except Exception as e:

    print(
        Fore.RED +
        f"\nError: {e}"
    )

input(
    Fore.YELLOW +
    "\nPress ENTER to return to toolkit..."
)
