# A package is a collection of modules
# This module is part of the package "museum"
import requests

def get_artists(query, limit):
    # Request data from the artic api
    try:
        response = requests.get("https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit})
        # If the request didn't go through, raise an HTTPError
        response.raise_for_status()
    except requests.HTTPError:
        # If there was an HTTP error, return an empty list
        return []
    
    # Convert the response into json format
    content = response.json()
    # Return a list of artists
    return [artist["title"] for artist in content["data"]]