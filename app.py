from tools import subdomain_finder , header_scanner, port_scanner, geolocation
import os
from colorama import Fore, init

init(autoreset=True)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.LIGHTMAGENTA_EX}\n------------------------------------")
    print(f"{Fore.LIGHTMAGENTA_EX}|  BUG HUNTER TOOLBOX - CLI (v1.0) |")
    print(f"{Fore.LIGHTMAGENTA_EX}|          by stashEmal            |")
    print(f"{Fore.LIGHTMAGENTA_EX}------------------------------------\n")

    print("1. Subdomain Finder")
    print("2. HTTP Header Scanner")
    print("3. Port Scanner")
    print("4. IP Geolocation")
    
    choice = input("\nEnter your choice > ")
    if choice == '1':
        subdomain_finder.main()
    elif choice == '2':
        header_scanner.main()
    elif choice == '3':
        port_scanner.main()
    elif choice == '4':
        geolocation.main()
    else:
        print("Invalid choice. Quitting...")

if __name__ == '__main__':
    main()