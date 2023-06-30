from utils import get_app_logger


class BaseController:
    
    """
    A base class for controllers.
    """
    
    def __init__(self):
        """
        Initialize the base controller.
        """
        self.logger = get_app_logger()