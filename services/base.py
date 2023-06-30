from utils import get_app_logger


class BaseService:
    """
    A base class for services.
    """

    def __init__(self):
        """
        Initialize the base service.
        """
        self.logger = get_app_logger()