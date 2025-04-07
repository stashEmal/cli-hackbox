import requests
from urllib.parse import urlparse
from colorama import Fore, init
import os

init(autoreset=True)

# List of security headers to check
SECURITY_HEADERS = {
    "Content-Security-Policy": "Prevents XSS & data injection attacks",
    "Strict-Transport-Security": "Enforces HTTPS",
    "X-Content-Type-Options": "Prevents MIME-sniffing",
    "X-Frame-Options": "Protects against clickjacking",
    "X-XSS-Protection": "Enables XSS filter in some browsers (deprecated)",
    "Referrer-Policy": "Controls information sent in the Referer header",
    "Permissions-Policy": "Restricts browser features",
}

def validate_url(url):
    """Validate and normalize the input URL."""
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "http://" + url  # Default to HTTP if no scheme is provided
    return url

def fetch_headers(url):
    """Fetch HTTP response headers for the given URL."""
    try:
        response = requests.get(url, timeout=5)
        return response.headers
    except requests.exceptions.RequestException as e:
        print(f"[!] Error fetching headers: {e}")
        return None

def analyze_headers(headers):
    """Analyze the presence of security headers."""
    print("\n[+] Analyzing security headers...\n")
    for header, purpose in SECURITY_HEADERS.items():
        if header in headers:
            print(f"{Fore.RED}✓ {header}: present ({purpose})")
        else:
            print(f"{Fore.GREEN}✗ {header}: MISSING ({purpose})")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    """Main function to run the header scanner."""
    print(f"{Fore.LIGHTCYAN_EX}\n------------------------------------")
    print(f"{Fore.LIGHTCYAN_EX}|       HTTP HEADER SCANNER        |")
    print(f"{Fore.LIGHTCYAN_EX}|          by stashEmal            |")
    print(f"{Fore.LIGHTCYAN_EX}------------------------------------\n")

    # Get the target URL from the user
    url = input("Enter the target URL (e.g., https://example.com): ").strip()
    if not url:
        print("[!] Error: URL cannot be empty!")
        return

    # Validate and normalize the URL
    url = validate_url(url)
    print(f"\n[+] Scanning headers for: {url}\n")

    # Fetch headers
    headers = fetch_headers(url)
    if headers:
        # Analyze headers
        analyze_headers(headers)
        print("\n[+] Scan complete!")
    else:
        print("[!] Failed to fetch headers. Exiting.")

if __name__ == "__main__":
    main()