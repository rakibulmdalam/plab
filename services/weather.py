import json
import requests
from typing import Optional
import redis
from configs.project_config import ProjectConfig
from services.base import BaseService


class WeatherService(BaseService):
    """
    A service class to interact with the WeatherAPI and retrieve weather data.
    """

    def __init__(self):
        """
        Initialize the WeatherService by loading the API key from environment variables
        and setting up the Redis caching client.
        """
        self.api_key = ProjectConfig().WEATHERAPI_API_KEY
        self.base_url = ProjectConfig().WEATHER_API_BASE_URL
        self.redis_client = redis.Redis(
            host=ProjectConfig().REDIS_HOST, port=ProjectConfig().REDIS_PORT
        )  # Configure Redis connection
        super().__init__()

    def get_weather_by_location(self, location: str) -> Optional[dict]:
        """
        Retrieve weather data for a specific location from the WeatherAPI.

        Args:
            location: The location for which to retrieve weather data.

        Returns:
            A dictionary containing the weather data for the specified location, or None if an error occurred.
        """
        cached_weather = self.redis_client.get(location)
        if cached_weather:
            self.logger.debug(f"Retrieved weather data for {location} from cache.")
            cached_weather = json.loads(cached_weather)
            cached_weather["source"] = "cache"
            return cached_weather

        try:
            if self.api_key is None:
                self.logger.error(
                    "WeatherAPI API key not found. Make sure to set the WEATHERAPI_API_KEY environment variable."
                )
                raise WeatherAPIKeyMissingError()

            url = f"{self.base_url}/current.json"
            params = {"key": self.api_key, "q": location}
            response = requests.get(url, params=params)
            if response.status_code == 200:
                weather_data = response.json()
                self.redis_client.set(
                    location, json.dumps(weather_data), ex=ProjectConfig().CACHE_TIMEOUT
                )  # Cache data for 2 hours
                weather_data["source"] = "api"
                return weather_data
            else:
                self.logger.debug(f"Failed to retrieve weather data for {location}.")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred during the weather API request: {e}")

        return None


class WeatherAPIKeyMissingError(Exception):
    """Raised when the WeatherAPI API key is missing."""

    pass
