import requests
import json

from catalyst_center_utils import *

# Disable SSL warnings (only use this in testing environments)
requests.packages.urllib3.disable_warnings()

# API details
BASE_URL = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

def main():
    # Get authentication token
    token = get_auth_token(BASE_URL, USERNAME, PASSWORD)
    
    devices_url = f"{BASE_URL}/dna/intent/api/v1/client-health"
    
    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(
            devices_url,
            headers=headers,
            verify=False  # Disable SSL verification (only for testing)
        )
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=4))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()