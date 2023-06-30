import pytest
from models.shipment import Shipment
from models.item import Item
from services.shipments import ShipmentsService


# Create sample shipment data
shipment_data = {
    "tracking_number": "123456789",
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
    "status": "Delivered"
}

@pytest.fixture
def shipment_service():
    # Create a ShipmentsService instance
    service = ShipmentsService()
    
    # Yield the service to the test case
    yield service
    
    # Perform teardown after the test case is executed
    # Delete the test data from the database
    service.shipment_repository.delete_by_tracking_number("123456789")


class TestShipmentService:
    def test_get_shipment_by_tracking_number(self, shipment_service):
        
        # Add the sample shipment to the repository
        shipment_service.create_shipment(shipment_data)
        
        # Call the method under test
        result = shipment_service.get_shipment_by_tracking_number("123456789")
        
        # Assert the result
        assert isinstance(result, Shipment)
        assert result.tracking_number == "123456789"
        assert result.carrier == "UPS"
        assert result.sender_address == "123 Main St"
        assert result.receiver_address == "456 Elm St"
        assert len(result.items) == 2
        assert isinstance(result.items[0], Item)
        assert isinstance(result.items[1], Item)
        assert result.status == "Delivered"
