from flask import Flask, json
from flask_restful import Api

from resources.user import User

from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv(".env")
app.config.from_object("default_config")
app.config.from_envvar("APPLICATION_SETTINGS")

api = Api(app)

api.add_resource(User, "/", endpoint = 'user')

if __name__ == "__main__":
    app.run(port=5000, debug=True)