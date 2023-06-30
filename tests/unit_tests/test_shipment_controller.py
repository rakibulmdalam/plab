import pytest
from unittest.mock import MagicMock
from controllers.shipments import ShipmentController
from services.shipments import ShipmentsService
from services.weather import WeatherAPIKeyMissingError, WeatherService

class TestShipmentController:

    @pytest.fixture
    def shipment_controller(self):
        return ShipmentController()

    def test_track_shipment_with_valid_params(self, shipment_controller, monkeypatch):
        params = {
            "tracking_number": "TN123456789",
            "carrier": "UPS"
        }

        shipment_service_mock = ShipmentsService  # Create an instance of ShipmentsService
        weather_service_mock = WeatherService  # Create an instance of WeatherService

        shipment_mock = MagicMock()
        shipment_mock.to_dict.return_value = {"tracking_number": "TN123456789"}

        weather_data_mock = {"location": "New York", "temperature": 25}

        monkeypatch.setattr(
            shipment_service_mock,
            "get_shipment_by_tracking_number_and_carrier",
            MagicMock(return_value=shipment_mock)
        )
        monkeypatch.setattr(
            weather_service_mock,
            "get_weather_by_location",
            MagicMock(return_value=weather_data_mock)
        )

        shipment_controller.shipment_service = shipment_service_mock
        shipment_controller.weather_service = weather_service_mock

        response, status_code = shipment_controller.track_shipment(params)

        assert status_code == 200
        assert "shipment" in response
        assert "weather" in response
        assert response["shipment"] == {"tracking_number": "TN123456789"}
        assert response["weather"] == weather_data_mock

    def test_track_shipment_missing_tracking_number(self, shipment_controller):
        params = {}

        response, status_code = shipment_controller.track_shipment(params)

        assert status_code == 400
        assert response == {"msg": "Tracking number not provided"}

    def test_track_shipment_shipment_not_found(self, shipment_controller, monkeypatch):
        params = {"tracking_number": "TN123456789"}

        shipment_service_mock = ShipmentsService
        
        monkeypatch.setattr(
            shipment_service_mock,
            "get_shipment_by_tracking_number_and_carrier",
            MagicMock(return_value=None)
        )

        response, status_code = shipment_controller.track_shipment(params)

        assert status_code == 404
