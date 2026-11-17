import shutil
import time
from colorama import Fore, init

init(autoreset=True)

print(Fore.CYAN + """
========================================
          PROJECT BACKUP
========================================
""")

backup_name = f"toolkit_backup_{int(time.time())}"

shutil.make_archive(
    backup_name,
    "zip",
    "."
)

print(
    Fore.GREEN +
    f"\nBackup created: {backup_name}.zip"
)

input(
    Fore.YELLOW +
    "\nPress ENTER to return..."
)
