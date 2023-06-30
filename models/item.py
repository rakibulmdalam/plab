from typing import Dict, Any


class Item:
    def __init__(self, name: str, quantity: int, price: float, SKU: str) -> None:
        self.article_name = name
        self.article_quantity = quantity
        self.article_price = price
        self.SKU = SKU

    def to_dict(self) -> Dict[str, Any]:
        return {
            "article_name": self.article_name,
            "article_quantity": self.article_quantity,
            "article_price": self.article_price,
            "SKU": self.SKU,
        }
