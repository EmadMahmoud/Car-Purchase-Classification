from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView
import model
from schemas import PredictSchema

blp = Blueprint("Prediction Endpoint", __name__, description="No description")


@blp.route("/predict")
class Predict(MethodView):
    @blp.arguments(PredictSchema)
    def post(self, request_data):
        result = model.classifier.predict(
            model.sc.transform([[request_data["age"], request_data["salary"]]])).tolist()
        return result, 201

