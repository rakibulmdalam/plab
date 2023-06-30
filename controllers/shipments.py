from controllers.base import BaseController
from services.shipments import ShipmentsService
from services.weather import WeatherAPIKeyMissingError, WeatherService


class ShipmentController(BaseController):
    def __init__(self):
        super().__init__()

    def track_shipment(self, params) -> dict:
        shipment_service = ShipmentsService()
        weather_service = WeatherService()

        if "tracking_number" not in params:
            response_data = {"msg": "Tracking number not provided"}
            return response_data, 400

        if "carrier" in params:
            print("carrier in params")
            shipment = shipment_service.get_shipment_by_tracking_number_and_carrier(
                params["tracking_number"], params["carrier"]
            )
        else:
            shipment = shipment_service.get_shipment_by_tracking_number(
                params["tracking_number"]
            )

        if shipment is None:
            response_data = {"msg": "Shipment not found"}
            return response_data, 404

        # Fetch weather data for the shipment location
        location = shipment.receiver_address.split(",")[-2].split(" ")[-1].strip()
        weather_data = None
        try:
            weather_data = weather_service.get_weather_by_location(location)
            # TODO: Handle weather data not found
        except WeatherAPIKeyMissingError as e:
            self.logger.debug("An error occurred while retrieving weather data: {e}")

        response_data = {"shipment": shipment.to_dict(), "weather": weather_data}

        return response_data, 200
