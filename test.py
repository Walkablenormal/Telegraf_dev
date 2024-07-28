import requests
import json
import sys
from fetch_catalyst_token import *
# Disable SSL warnings (only use this in testing environments)
requests.packages.urllib3.disable_warnings()

# API details
BASE_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

token = get_auth_token(base_url=BASE_URL, username=USERNAME, password=PASSWORD)

def get_devices(token):
    """
    Get device data using the authentication token.
    """
    devices_url = f"{BASE_URL}/dna/intent/api/v1/network-device"
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(
            devices_url,
            headers=headers,
            verify=False  # Disable SSL verification (only for testing)
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching devices: {e}")
        sys.exit(1)

def main():
    # Get authentication token
    token = get_auth_token()

    # Get device data
    devices_data = get_devices(token)

    # Print JSON data
    print(json.dumps(devices_data, indent=2))

if __name__ == "__main__":
    main()
