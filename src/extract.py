import requests
import json
from pathlib import Path

API_URL = "https://api.openbrewerydb.org/v1/breweries"

def fetch_breweries():
    page = 1
    all_data = []

    while True:
        response = requests.get(API_URL, params={"page": page, "per_page": 200})

        if response.status_code != 200:
            raise Exception("API request failed")

        data = response.json()

        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data

def save_raw(data, path="data/bronze/breweries_raw.json"):
    Path("data/bronze").mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f)
