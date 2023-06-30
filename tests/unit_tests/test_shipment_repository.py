from models.shipment import Shipment
from repositories.shipments import ShipmentRepository
import pytest


shipment_data = {
    "tracking_number": "1234567829",
    "carrier": "UPS",
    "sender_address": "123 Main St",
    "receiver_address": "456 Elm St",
    "items": [
                {
                    "article_name": "Item 1",
                    "article_quantity": 2,
                    "article_price": 10.99,
                    "SKU": "ABC123"
                },
                {
                    "article_name": "Item 2",
                    "article_quantity": 3,
                    "article_price": 5.99,
                    "SKU": "DEF456"
                }
            ],
    "status": "Pending",
}


@pytest.fixture
def shipment_repository(request):
    # Create a ShipmentRepository instance
    repository = ShipmentRepository()

    # Define the teardown function
    def teardown():
        # Delete the test data from the database
        repository.delete_by_tracking_number("1234567829")

    # Register the teardown function as the finalizer
    request.addfinalizer(teardown)

    return repository


class TestShipmentRepository:
    def test_create_shipment(self, shipment_repository):
        # Create a Shipment instance
        shipment = Shipment.from_dict(shipment_data)

        # Call the method under test
        result = shipment_repository.create(shipment)

        # Assert the result
        assert result is True

    def test_get_shipment_by_tracking_number(self, shipment_repository):
        
        # Create a Shipment instance
        shipment = Shipment.from_dict(shipment_data)

        # Call the method under test
        result = shipment_repository.create(shipment)
        
        # Call the method under test
        result = shipment_repository.get_shipment_by_tracking_number("1234567829")

        # Assert the result
        assert isinstance(result, Shipment)
        assert result.tracking_number == "1234567829"

    def test_get_all_shipments(self, shipment_repository):
        # Call the method under test
        result = shipment_repository.get_all()

        # Assert the result
        assert isinstance(result, list)
        assert all(isinstance(shipment, Shipment) for shipment in result)

    def test_update_shipment(self, shipment_repository):
        
        # Create a Shipment instance
        shipment = Shipment.from_dict(shipment_data)

        # Call the method under test
        result = shipment_repository.create(shipment)

        # Update the shipment's status
        shipment.status = "Delivered"

        # Call the method under test
        result = shipment_repository.update(shipment)

        # Assert the result
        assert result is True

    def test_delete_shipment_by_tracking_number(self, shipment_repository):
        # Call the method under test
        result = shipment_repository.delete_by_tracking_number("1234567829")

        # Assert the result
        assert result is True
