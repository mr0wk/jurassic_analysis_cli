import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")


def stringify_dinosaur(dinosaur):
    return f"{dinosaur['name'].capitalize()} lived in the {dinosaur['period']} period and was a {dinosaur['diet']}. It was {dinosaur['length']} meters long. It lived in {dinosaur['lived_in']}. It was a {dinosaur['type']} and was a {dinosaur['species']}."


def read_dinosaurs_by_properties(property_value_dict: dict):
    url = f"{API_URL}?"
    for property_name, property_value in property_value_dict.items():
        url += f"{property_name}={property_value}&"

    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: {response.status_code}"

    data = json.loads(response.text)
    return data


def read_dinosaurs():
    response = requests.get(API_URL)
    data = json.loads(response.text)

    return data
