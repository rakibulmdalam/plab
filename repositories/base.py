from abc import ABC, abstractmethod
from typing import Any, Optional, List

from utils import get_app_logger


class BaseRepository(ABC):
    
    def __init__(self):
        """
        Initializes a new instance of BaseRepository.
        """
        self.logger = get_app_logger()
        
    @abstractmethod
    def create(self, item: Any) -> bool:
        """
        Create a new item in the repository.

        Args:
            item: The item to be created.

        Returns:
            bool: True if the item was created successfully, False otherwise.
        """
        pass

    @abstractmethod
    def get(self, id: str) -> Optional[Any]:
        """
        Retrieve an item from the repository based on its ID.

        Args:
            id: The ID of the item to retrieve.

        Returns:
            Optional[Any]: The retrieved item if found, None otherwise.
        """
        pass

    @abstractmethod
    def update(self, item: Any) -> bool:
        """
        Update an existing item in the repository.

        Args:
            item: The item to be updated.

        Returns:
            bool: True if the item was updated successfully, False otherwise.
        """
        pass

    @abstractmethod
    def delete(self, id: str) -> bool:
        """
        Delete an item from the repository based on its ID.

        Args:
            id: The ID of the item to delete.

        Returns:
            bool: True if the item was deleted successfully, False otherwise.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        """
        Retrieve all items from the repository.

        Returns:
            List[Any]: A list of all items in the repository.
        """
        pass
