from flask import Flask
from flask_smorest import Api
from resources.prediction import blp as PredictBlueprint

app = Flask(__name__)

app.config["API_TITLE"] = "Car Purchase REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(PredictBlueprint)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

