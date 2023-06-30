from typing import List, Optional
from tinydb import TinyDB, Query
from configs.project_config import ProjectConfig
from models.shipment import Shipment
from repositories.base import BaseRepository


class ShipmentRepository(BaseRepository):
    """
    Repository class for managing shipments.
    """

    def __init__(self):
        """
        Initializes a new instance of ShipmentRepository.
        """
        self.db = TinyDB(ProjectConfig().DB)
        self.shipments_table = self.db.table(ProjectConfig().SHIPMENTS_TABLE_NAME)
        super().__init__()

    def create(self, shipment: Shipment) -> bool:
        """
        Creates a new shipment.

        Args:
            shipment: The shipment object to create.

        Returns:
            bool: True if the shipment was created successfully, False otherwise.
        """
        try:
            shipment_data = shipment.to_dict()
            self.shipments_table.insert(shipment_data)
            return True
        except Exception as e:
            self.logger.error(f"An error occurred while creating the shipment: {e}")
            return False

    def get(self, id: str) -> Optional[Shipment]:
        """
        Retrieves a shipment by ID.

        Args:
            id: The ID of the shipment to retrieve.

        Returns:
            Optional[Shipment]: The shipment object if found, None otherwise.
        """
        shipment_query = Query()
        try:
            shipment_data = self.shipments_table.get(
                shipment_query.tracking_number == id
            )
            if shipment_data:
                shipment = Shipment.from_dict(shipment_data)  # type: ignore
                return shipment
        except Exception as e:
            self.logger.error(f"An error occurred while retrieving the shipment: {e}")

        return None

    def get_all(self) -> List[Shipment]:
        """
        Retrieves all shipments.

        Returns:
            List[Shipment]: A list of all shipments.
        """
        try:
            shipments_data = self.shipments_table.all()
            shipments = []
            for shipment_data in shipments_data:
                shipment = Shipment.from_dict(shipment_data)
                shipments.append(shipment)
            return shipments
        except Exception as e:
            self.logger.error(f"An error occurred while retrieving the shipments: {e}")

        return []

    def get_shipment_by_tracking_number(
        self, tracking_number: str
    ) -> Optional[Shipment]:
        """
        Retrieves a shipment by tracking number.

        Args:
            tracking_number: The tracking number of the shipment to retrieve.

        Returns:
            Optional[Shipment]: The shipment object if found, None otherwise.
        """
        return self.get(tracking_number)

    def get_shipment_by_tracking_number_and_carrier(
        self, tracking_number: str, carrier: str
    ) -> Optional[Shipment]:
        """
        Retrieves a shipment by tracking number and carrier.

        Args:
            tracking_number: The tracking number of the shipment to retrieve.
            carrier: The carrier of the shipment to retrieve.

        Returns:
            Optional[Shipment]: The shipment object if found, None otherwise.
        """
        shipment_query = Query()
        try:
            shipment_data = self.shipments_table.get(
                (shipment_query.tracking_number == tracking_number)
                & (shipment_query.carrier == carrier)
            )
            if shipment_data:
                shipment = Shipment.from_dict(shipment_data)
                return shipment
        except Exception as e:
            self.logger.error(f"An error occurred while retrieving the shipment: {e}")

        return None

    def update(self, shipment: Shipment) -> bool:
        """
        Updates an existing shipment.

        Args:
            shipment: The shipment object with updated data.

        Returns:
            bool: True if the shipment was updated successfully, False otherwise.
        """
        try:
            shipment_data = shipment.to_dict()
            shipment_query = Query()
            self.shipments_table.update(
                shipment_data,
                shipment_query.tracking_number == shipment.tracking_number,
            )
            return True
        except Exception as e:
            self.logger.error(f"An error occurred while updating the shipment: {e}")
            return False

    def delete(self, id: str) -> bool:
        """
        Deletes a shipment by ID.

        Args:
            id: The ID of the shipment to delete.

        Returns:
            bool: True if the shipment was deleted successfully, False otherwise.
        """
        shipment_query = Query()
        try:
            self.shipments_table.remove(shipment_query.tracking_number == id)
            return True
        except Exception as e:
            self.logger.error(f"An error occurred while deleting the shipment: {e}")
            return False

    def delete_by_tracking_number(self, tracking_number: str) -> bool:
        """
        Deletes a shipment by tracking number.

        Args:
            tracking_number: The tracking number of the shipment to delete.

        Returns:
            bool: True if the shipment was deleted successfully, False otherwise.
        """
        return self.delete(tracking_number)
