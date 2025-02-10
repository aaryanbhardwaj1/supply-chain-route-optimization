import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

UPS_CLIENT_ID = os.getenv("UPS_CLIENT_ID")
UPS_CLIENT_SECRET = os.getenv("UPS_CLIENT_SECRET")

class UPSAPI:
    """
    Handles authentication and transit time fetching from UPS API.
    """

    TOKEN_URL = "https://wwwcie.ups.com/security/v1/oauth/token"
    TRANSIT_URL = "https://onlinetools.ups.com/rest/TimeInTransit"

    def __init__(self):
        """
        Initializes the UPS API handler and retrieves an access token.
        """
        self.access_token = None
        self.authenticate()

    def authenticate(self):
        """
        Obtains an access token from the UPS API.
        """
        payload = {"grant_type": "client_credentials"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        
        response = requests.post(self.TOKEN_URL, data=payload, headers=headers, auth=(UPS_CLIENT_ID, UPS_CLIENT_SECRET))
        
        if response.status_code == 200:
            self.access_token = response.json().get("access_token")
        else:
            raise Exception(f"Failed to authenticate with UPS API: {response.text}")

    def get_transit_time(self, origin, destination):
        """
        Fetches the transit time between two UPS locations.

        Parameters:
        - origin (dict): {"postalCode": "12345", "countryCode": "US"}
        - destination (dict): {"postalCode": "67890", "countryCode": "US"}

        Returns:
        - dict: UPS transit time response.
        """
        if not self.access_token:
            self.authenticate()

        headers = {"Authorization": f"Bearer {self.access_token}"}
        payload = {
            "request": {
                "shipment": {
                    "origin": origin,
                    "destination": destination
                }
            }
        }

        response = requests.post(self.TRANSIT_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch transit time: {response.text}")

# Usage Example
if __name__ == "__main__":
    ups_api = UPSAPI()
    origin = {"postalCode": input("Enter origin postal code: ").strip(), "countryCode": "US"}
    destination = {"postalCode": input("Enter destination postal code: ").strip(), "countryCode": "US"}

    try:
        transit_info = ups_api.get_transit_time(origin, destination)
        print("Transit Time Data:", transit_info)
    except Exception as e:
        print("Error:", e)
