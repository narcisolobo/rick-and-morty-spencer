import requests
from pprint import pprint
from flask import Blueprint, redirect, render_template, request, session

bp = Blueprint("characters", __name__)


@bp.get("/")
def home():
    """ Displays the home template. """

    return render_template("home.html")


@bp.get("/characters")
def all_characters():
    """ Displays the all_characters template. """

    if not 'endpoint' in session:
        session['endpoint'] = "https://rickandmortyapi.com/api/character"

    response = requests.get(session['endpoint'])

    print(f"Status Code: {response.status_code}")
    print(f"URL: {response.url}")

    data = response.json()
    info = data["info"]
    results = data["results"]

    characters = []
    for result in results:
        character = {
            "id": result["id"],
            "name": result["name"],
            "image": result["image"],
            "gender": result["gender"],
            "species": result["species"],
            "created": result["created"],
        }
        characters.append(character)

    return render_template("all_characters.html", characters=characters, info=info)


@bp.post("/url/set")
def set_url():
    """ Sets the next endpoint for API call. """

    session["endpoint"] = request.form["url"]
    return redirect("/characters")


@bp.get("/clear-session")
def clear_session():
    """ Clears the session data. """

    session.clear()
    return redirect("/characters")
