import requests

class InstagramAPI:
    """
    Class for Instagram API.
    """
    def __init__(self, access_token):
        self.base_url = "https://graph.instagram.com"
        self.access_token = access_token

    def search_city_places(self, city_name):
        """
        Search for popular places in a city.
        """
        # Mock API endpoint; replace with actual endpoint.
        url = f"{self.base_url}/search?type=place&q={city_name}&access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError("Failed to fetch places from Instagram API.")
        data = response.json()
        return data.get("data", [])

    def fetch_place_photos(self, place_id):
        """
        Fetch photos for a given place.
        """
        # Mock API endpoint; replace with actual endpoint.
        url = f"{self.base_url}/{place_id}/media?access_token={self.access_token}"
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError("Failed to fetch photos for the place.")
        data = response.json()
        return data.get("data", [])
