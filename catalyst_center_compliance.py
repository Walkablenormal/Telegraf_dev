import sys
import json
import requests

from catalyst_center_utils import get_auth_token
from config import BASE_URL, USERNAME, PASSWORD, SSL_VERIFY

def main():
    """
    Returns physical topology information from Catalyst Center.
    """
    # Get authentication token
    token = get_auth_token(BASE_URL, USERNAME, PASSWORD)

    devices_url = f"{BASE_URL}/dna/intent/api/v1/compliance"

    headers = {
        "X-Auth-Token": token,
        "Content-Type": "application/json",
    }
    try:
        response = requests.get(
            devices_url,
            headers=headers,
            verify=SSL_VERIFY,
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=4))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
