from typing import Dict, List, Optional
from models.shipment import Shipment
from repositories.shipments import ShipmentRepository
from services.base import BaseService


class ShipmentsService(BaseService):
    """
    Service class for managing shipments.
    """

    def __init__(self):
        """
        Initializes a new instance of ShipmentService.
        """
        self.shipment_repository = ShipmentRepository()
        super().__init__()

    def create_shipment(self, shipment: Dict) -> bool:
        """
        Creates a new shipment.

        Args:
            shipment: A dictionary containing shipment data.

        Returns:
            bool: True if the shipment was created successfully, False otherwise.
        """
        return self.shipment_repository.create(Shipment.from_dict(shipment))

    def get_all_shipments(self) -> List[Shipment]:
        """
        Retrieves all shipments.

        Returns:
            List[Shipment]: A list of all shipments.
        """
        return self.shipment_repository.get_all()

    def get_shipment_by_tracking_number(
        self, tracking_number: str
    ) -> Optional[Shipment]:
        """
        Retrieves a shipment by its tracking number.

        Args:
            tracking_number: The tracking number of the shipment.

        Returns:
            Optional[Shipment]: The shipment object if found, None otherwise.
        """
        return self.shipment_repository.get_shipment_by_tracking_number(tracking_number)

    def get_shipment_by_tracking_number_and_carrier(
        self, tracking_number: str, carrier_code
    ) -> Optional[Shipment]:
        """
        Retrieves a shipment by its tracking number and carrier code.

        Args:
            tracking_number: The tracking number of the shipment.
            carrier_code: The carrier code of the shipment.

        Returns:
            Optional[Shipment]: The shipment object if found, None otherwise.
        """
        return self.shipment_repository.get_shipment_by_tracking_number_and_carrier(
            tracking_number, carrier_code
        )

    def update_shipment(self, shipment: Dict) -> bool:
        """
        Updates an existing shipment.

        Args:
            shipment: A dictionary containing updated shipment data.

        Returns:
            bool: True if the shipment was updated successfully, False otherwise.
        """
        return self.shipment_repository.update(Shipment.from_dict(shipment))

    def delete_shipment_by_tracking_number(self, tracking_number: str) -> bool:
        """
        Deletes a shipment by its tracking number.

        Args:
            tracking_number: The tracking number of the shipment.

        Returns:
            bool: True if the shipment was deleted successfully, False otherwise.
        """
        return self.shipment_repository.delete_by_tracking_number(tracking_number)
