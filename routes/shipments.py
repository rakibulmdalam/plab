from flask import Blueprint
from controllers.shipments import ShipmentController
from flask_restx import Namespace, Resource, fields

from configs.namespace_config import NamespaceConfig

SHIPMENT_API = Blueprint("SHIPMENT_API", __name__)


def get_blueprint():
    return SHIPMENT_API


shipment_api = Namespace(
    "shipments",
    description="All Shipments related operations",
    path=NamespaceConfig().SHIPMENTS_PATH,
)


# Define the API models
track_shipment_payload_model = shipment_api.model(
    "TrackPayload",
    {
        "tracking_number": fields.String(
            required=True, description="Tracking number of the shipment"
        ),
        "carrier": fields.String(required=True, description="Carrier of the shipment"),
    },
)


@shipment_api.route("/track/<tracking_number>")
@shipment_api.param("tracking_number", "The tracking number of the shipment")
class TrackShipment(Resource):
    @shipment_api.response(200, "Success")
    @shipment_api.response(400, "Tracking number not provided")
    @shipment_api.response(404, "Shipment not found")
    @shipment_api.response(500, "Internal Server Error")
    def get(self, tracking_number):
        """
        Retrieve information about a shipment by tracking number.
        """
        params = {"tracking_number": tracking_number}
        response_data, status_code = ShipmentController().track_shipment(params)
        return response_data, status_code


@shipment_api.route("/track/<tracking_number>/<carrier>")
@shipment_api.param("tracking_number", "The tracking number of the shipment")
@shipment_api.param("carrier", "The carrier of the shipment")
class TrackShipmentWithCarrier(Resource):
    @shipment_api.response(200, "Success")
    @shipment_api.response(400, "Tracking number not provided")
    @shipment_api.response(404, "Shipment not found")
    @shipment_api.response(500, "Internal Server Error")
    def get(self, tracking_number, carrier):
        """
        Retrieve information about a shipment by tracking number and carrier.
        """
        params = {"tracking_number": tracking_number, "carrier": carrier}
        response_data, status_code = ShipmentController().track_shipment(params)
        return response_data, status_code


@shipment_api.route("/track/", methods=["POST"])
class TrackShipmentByPost(Resource):
    @shipment_api.expect(track_shipment_payload_model)
    @shipment_api.response(200, "Success")
    @shipment_api.response(400, "Tracking number not provided")
    @shipment_api.response(404, "Shipment not found")
    @shipment_api.response(500, "Internal Server Error")
    def post(self):
        """
        Send a POST request to retrieve information about a shipment by tracking number and carrier.
        """
        params = shipment_api.payload
        response_data, status_code = ShipmentController().track_shipment(params)
        return response_data, status_code


# Add resource classes to the API
shipment_api.add_resource(TrackShipment, "/track/<tracking_number>")
shipment_api.add_resource(
    TrackShipmentWithCarrier, "/track/<tracking_number>/<carrier>"
)
shipment_api.add_resource(TrackShipmentByPost, "/track/")
