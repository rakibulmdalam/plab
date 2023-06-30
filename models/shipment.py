from typing import Dict, List, Optional, Any

from models.item import Item
from utils import get_app_logger

logger = get_app_logger()


class Shipment:
    def __init__(
        self,
        tracking_number: str,
        carrier: str,
        sender_address: str,
        receiver_address: str,
        items: List[Item],
        status: str,
    ) -> None:
        self.tracking_number = tracking_number
        self.carrier = carrier
        self.sender_address = sender_address
        self.receiver_address = receiver_address
        self.items = items
        self.status = status

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Optional["Shipment"]:
        tracking_number = data.get("tracking_number")
        carrier = data.get("carrier")
        sender_address = data.get("sender_address")
        receiver_address = data.get("receiver_address")
        items_data = data.get("items")
        status = data.get("status")

        if not (
            tracking_number
            and carrier
            and sender_address
            and receiver_address
            and items_data
            and status
        ):
            logger.error("Invalid shipment data")
            return None

        items = []
        for item_data in items_data:
            article_name = item_data.get("article_name")
            article_quantity = item_data.get("article_quantity", 0)
            article_price = item_data.get("article_price", 0.0)
            SKU = item_data.get("SKU")

            if not (article_name and article_quantity and article_price and SKU):
                logger.error("Invalid item data")
                return None

            item = Item(article_name, article_quantity, article_price, SKU)
            items.append(item)

        return cls(
            tracking_number, carrier, sender_address, receiver_address, items, status
        )

    def to_dict(self) -> Dict[str, Any]:
        items_data = [item.to_dict() for item in self.items]

        return {
            "tracking_number": self.tracking_number,
            "carrier": self.carrier,
            "sender_address": self.sender_address,
            "receiver_address": self.receiver_address,
            "items": items_data,
            "status": self.status,
        }
