import requests
from pprint import pprint
from flask import Blueprint, render_template

bp = Blueprint("characters", __name__)


@bp.get("/")
def home():
    """ Displays the home template. """

    return render_template("home.html")


@bp.get("/characters")
def all_characters():
    """ Displays the all_characters template. """

    endpoint = "https://rickandmortyapi.com/api/character"

    response = requests.get(endpoint)

    print(f"Status Code: {response.status_code}")
    print(f"URL: {response.url}")

    data = response.json()
    pprint(data)

    results = data["results"]
    characters = []

    for result in results:
        character = {
            "id": result["id"],
            "name": result["name"],
            "image": result["image"],
            "gender": result["gender"],
            "species": result["species"],
        }
        characters.append(character)

    return render_template("all_characters.html", characters=characters)
