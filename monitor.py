import os
import time
import psutil
from colorama import Fore, init

# Initialize colors
init(autoreset=True)

# Save logs
logs = open("monitor_logs.txt", "a")

try:

    while True:

        # Clear terminal
        os.system("clear")

        # Banner
        print(Fore.CYAN + """
███╗   ███╗ ██████╗ ███╗   ██╗██╗████████╗ ██████╗ ██████╗
████╗ ████║██╔═══██╗████╗  ██║██║╚══██╔══╝██╔═══██╗██╔══██╗
██╔████╔██║██║   ██║██╔██╗ ██║██║   ██║   ██║   ██║██████╔╝
██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║   ██║   ██║██╔══██╗
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██║   ██║   ╚██████╔╝██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")

        print(Fore.GREEN + "=" * 60)
        print(Fore.YELLOW + "         LIVE SYSTEM MONITOR")
        print(Fore.GREEN + "=" * 60)

        # CPU usage
        cpu = psutil.cpu_percent(interval=1)

        # RAM usage
        ram = psutil.virtual_memory().percent

        # Disk usage
        disk = psutil.disk_usage('/').percent

        # Battery
        battery = psutil.sensors_battery()

        # Uptime
        boot_time = psutil.boot_time()

        uptime = time.time() - boot_time

        # Display info
        print(Fore.CYAN + f"\n[CPU USAGE] : {cpu}%")

        print(Fore.MAGENTA + f"[RAM USAGE] : {ram}%")

        print(Fore.YELLOW + f"[DISK USAGE] : {disk}%")

        if battery:

            print(
                Fore.GREEN +
                f"[BATTERY] : {battery.percent}%"
            )

        print(
            Fore.WHITE +
            f"[UPTIME] : {int(uptime)} seconds"
        )

        # Save logs
        logs.write("\n====================================\n")

        logs.write(f"CPU : {cpu}%\n")

        logs.write(f"RAM : {ram}%\n")

        logs.write(f"DISK : {disk}%\n")

        if battery:

            logs.write(
                f"BATTERY : {battery.percent}%\n"
            )

        logs.write(f"UPTIME : {int(uptime)}\n")

        # Exit instructions
        print(
            Fore.RED +
            "\nPress CTRL + C to return to toolkit"
        )

        # Delay
        time.sleep(2)

except KeyboardInterrupt:

    logs.close()

    print(
        Fore.GREEN +
        "\n\n[✓] Returning to toolkit..."
    )
