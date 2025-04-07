import requests
import socket
import os
from colorama import Fore, Back, Style, init

# Load default subdomains from the file
try:
    with open('default_subdomains.txt', 'r') as file:
        default_subdomains = file.read().strip().split()
except FileNotFoundError:
    print(f"{Fore.RED}Error: default_subdomains.txt file not found!{Style.RESET_ALL}")
    defaunt_subdomains = []
print(default_subdomains)

# Initialize colorama for colored output
init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the tool banner."""
    print(f"{Fore.LIGHTCYAN_EX}\n------------------------------------")
    print(f"{Fore.LIGHTCYAN_EX}|      SUBDOMAIN FINDER TOOL       |")
    print(f"{Fore.LIGHTCYAN_EX}|          by stashEmal            |")
    print(f"{Fore.LIGHTCYAN_EX}------------------------------------\n")

def get_subdomains():
    """Get the list of subdomains to scan."""
    use_default = input("Use default subdomains? (y/n): ").strip().lower()
    if use_default == 'y':
        return default_subdomains
    else:
        custom_subdomains = input("Enter subdomains separated by commas: ").strip().split(',')
        return [sub.strip() for sub in custom_subdomains if sub.strip()]

def check_subdomain(domain, subdomain):
    """Check if a subdomain exists and is reachable."""
    url = f"http://{subdomain}.{domain}"
    try:
        # Check if the subdomain resolves to an IP address
        socket.gethostbyname(f"{subdomain}.{domain}")
        try:
            # Send an HTTP request to the subdomain
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{Back.GREEN}{Fore.BLACK}Found: {url}{Style.RESET_ALL}")
            else:
                print(f"{Back.YELLOW}{Fore.BLACK}Not found: {url} (HTTP {response.status_code}){Style.RESET_ALL}")
        except requests.ConnectionError:
            print(f"{Back.RED}{Fore.WHITE}Connection error: {url}{Style.RESET_ALL}")
        except requests.Timeout:
            print(f"{Back.RED}{Fore.WHITE}Timeout error: {url}{Style.RESET_ALL}")
    except socket.gaierror:
        print(f"{Fore.RED}Subdomain does not exist: {url}")

def main():
    """Main function to run the subdomain finder."""
    clear_screen()
    print_banner()

    # Get the domain and subdomains
    domain = input("Enter the domain (e.g., example.com): ").strip()
    if not domain:
        print(f"{Fore.RED}Error: Domain cannot be empty!{Style.RESET_ALL}")
        return

    subdomains = get_subdomains()
    print(f"\nScanning subdomains for: {Fore.CYAN}{domain}{Style.RESET_ALL}\n")

    # Check each subdomain
    for subdomain in subdomains:
        check_subdomain(domain, subdomain)

    print("\n[+] Scan complete!")

if __name__ == "__main__":
    main()