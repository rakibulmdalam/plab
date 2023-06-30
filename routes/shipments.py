from flask import Blueprint
from controllers.shipments import ShipmentController
from flask_restx import Api, Resource, fields

SHIPMENT_API = Blueprint("SHIPMENT_API", __name__)
api = Api(SHIPMENT_API)

# Define the API models
track_shipment_payload_model = api.model(
    "TrackPayload",
    {
        "tracking_number": fields.String(
            required=True, description="Tracking number of the shipment"
        ),
        "carrier": fields.String(required=True, description="Carrier of the shipment"),
    },
)


@api.route("/track/<tracking_number>")
@api.param("tracking_number", "The tracking number of the shipment")
class TrackShipment(Resource):
    @api.response(200, "Success")
    @api.response(400, "Tracking number not provided")
    @api.response(404, "Shipment not found")
    @api.response(500, "Internal Server Error")
    def get(self, tracking_number):
        """
        Retrieve information about a shipment by tracking number.
        """
        params = {"tracking_number": tracking_number}
        response_data, status_code = ShipmentController().track_shipment(params)
        return response_data, status_code


@api.route("/track/<tracking_number>/<carrier>")
@api.param("tracking_number", "The tracking number of the shipment")
@api.param("carrier", "The carrier of the shipment")
class TrackShipmentWithCarrier(Resource):
    @api.response(200, "Success")
    @api.response(400, "Tracking number not provided")
    @api.response(404, "Shipment not found")
    @api.response(500, "Internal Server Error")
    def get(self, tracking_number, carrier):
        """
        Retrieve information about a shipment by tracking number and carrier.
        """
        params = {"tracking_number": tracking_number, "carrier": carrier}
        response_data, status_code = ShipmentController().track_shipment(params)
        return response_data, status_code


@api.route("/track/", methods=["POST"])
class TrackShipmentByPost(Resource):
    @api.expect(track_shipment_payload_model)
    @api.response(200, "Success")
    @api.response(400, "Tracking number not provided")
    @api.response(404, "Shipment not found")
    @api.response(500, "Internal Server Error")
    def post(self):
        """
        Send a POST request to retrieve information about a shipment by tracking number and carrier.
        """
        params = api.payload
        response_data, status_code = ShipmentController().track_shipment(params)
        return response_data, status_code


# Add resource classes to the API
api.add_resource(TrackShipment, "/track/<tracking_number>")
api.add_resource(TrackShipmentWithCarrier, "/track/<tracking_number>/<carrier>")
api.add_resource(TrackShipmentByPost, "/track/")


def get_blueprint():
    return SHIPMENT_API
