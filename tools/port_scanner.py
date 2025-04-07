import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import os
import threading

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

init(autoreset=True)

# List of common ports and their services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

# Create a lock for thread-safe printing
print_lock = threading.Lock()

def scan_port(target, port):
    """Scan a single port on the target."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            result = s.connect_ex((target, port))  # Attempt to connect
            with print_lock:  # Ensure only one thread prints at a time
                if result == 0:  # Port is open
                    service = COMMON_PORTS.get(port, "Unknown Service")
                    print(f"{Fore.RED}✔ {port} ({service}) is OPEN")
                else:
                    print(f"{Fore.GREEN}✘ {port} is CLOSED or FILTERED")
    except Exception as e:
        with print_lock:  # Ensure error messages are also thread-safe
            print(f"[!] Error scanning port {port}: {e}")

def main():
    """Main function to run the port scanner."""
    clear_screen()
    print(f"{Fore.LIGHTCYAN_EX}\n------------------------------------")
    print(f"{Fore.LIGHTCYAN_EX}|         PORT SCANNER TOOL        |")
    print(f"{Fore.LIGHTCYAN_EX}|          by stashEmal            |")
    print(f"{Fore.LIGHTCYAN_EX}------------------------------------\n")

    # Get the target from the user
    target = input("Enter the target (e.g., example.com or 192.168.1.1): ").strip()
    if not target:
        print("[!] Error: Target cannot be empty!")
        return

    # Resolve domain to IP if needed
    try:
        target_ip = socket.gethostbyname(target)
        print(f"\n[+] Scanning ports for: {target} ({target_ip})\n")
    except socket.gaierror:
        print("[!] Error: Unable to resolve target!")
        return

    # Define the ports to scan
    ports = list(COMMON_PORTS.keys())  # Scan only common ports
    print(f"[+] Scanning {len(ports)} common ports...\n")

    # Use ThreadPoolExecutor for faster scanning
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in ports:
            executor.submit(scan_port, target_ip, port)

    print("\n[+] Scan complete!")

if __name__ == "__main__":
    main()