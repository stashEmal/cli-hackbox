import requests
import os
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_geolocation(ip_address):
    """Fetch geolocation data for the given IP address or domain."""
    url = f"http://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "IP Address": data.get("ip", "N/A"),
                "City": data.get("city", "N/A"),
                "Region": data.get("region", "N/A"),
                "Country": data.get("country", "N/A"),
                "Location (Lat, Long)": data.get("loc", "N/A"),
                "Organization": data.get("org", "N/A"),
                "Hostname": data.get("hostname", "N/A")
            }
        else:
            return {"Error": f"Failed to fetch data. HTTP Status Code: {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"Error": f"An error occurred: {e}"}

def print_geolocation(data):
    """Print geolocation data in a readable format."""
    print("\nGeolocation Information:")
    for key, value in data.items():
        print(f"{key}: {value}")

def save_to_file(ip_address, data):
    """Save geolocation data to a file."""
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)
    file_path = os.path.join(reports_dir, f"{ip_address}_geolocation.txt")
    try:
        with open(file_path, "w") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
        print(f"\n[+] Results saved to: {file_path}")
    except Exception as e:
        print(f"[!] Error saving results: {e}")

def main():
    """Main function to run the geolocation tool."""
    clear_screen()
    print(f"{Fore.LIGHTCYAN_EX}\n------------------------------------")
    print(f"{Fore.LIGHTCYAN_EX}|       GEOLOCATION LOOKUP TOOL    |")
    print(f"{Fore.LIGHTCYAN_EX}|          by stashEmal            |")
    print(f"{Fore.LIGHTCYAN_EX}------------------------------------\n")

    # Get the IP address or domain from the user
    ip_address = input("Enter the IP address : ").strip()
    if not ip_address:
        print("[!] Error: IP address cannot be empty!")
        return

    print(f"\n[+] Fetching geolocation data for: {ip_address}\n")

    # Fetch geolocation data
    data = get_geolocation(ip_address)

    # Print the results
    print_geolocation(data)

    # Ask the user if they want to save the results
    save = input("\nDo you want to save the results to a file? (y/n): ").strip().lower()
    if save == "y":
        save_to_file(ip_address, data)
    print("\n[!] Exiting geolocation tool.")

if __name__ == "__main__":
    main()