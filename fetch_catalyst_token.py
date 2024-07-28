import requests
import json
import sys

# Disable SSL warnings (only use this in testing environments)
requests.packages.urllib3.disable_warnings()

def get_auth_token(base_url, username, password):
    """
    Authenticate with Cisco Catalyst Center and get a token.
    """
    auth_url = f"{BASE_URL}/dna/system/api/v1/auth/token"

    try:
        response = requests.post(
            auth_url,
            auth=(USERNAME, PASSWORD),
            verify=False  # Disable SSL verification (only for testing)
        )
        response.raise_for_status()
        return response.json()["Token"]
    except requests.exceptions.RequestException as e:
        print(f"Error obtaining auth token: {e}")
        sys.exit(1)
