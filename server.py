from os import environ
from app import create_app
from dotenv import load_dotenv

load_dotenv()

ENV = environ.get("ENV")

if __name__ == "__main__":
    app = create_app()
    app.run(host="localhost", port=5001, debug=ENV == "DEVELOPMENT")
