import pytest
import redis
from services.weather import WeatherAPIKeyMissingError, WeatherService

class TestWeatherService:

    @pytest.fixture
    def weather_service(self):
        return WeatherService()

    def test_redis_caching(self, weather_service):
        location = "New York"

        # Clear the cache (optional, to ensure a clean state)
        redis_client = redis.Redis()
        redis_client.delete(location)

        # Retrieve weather data for the location (should not be cached yet)
        result = weather_service.get_weather_by_location(location)

        # Check that the result is as expected
        assert result["source"] == "api"

        # Retrieve weather data again for the same location (should be cached)
        result_cached = weather_service.get_weather_by_location(location)

        # Check that the cached result is the same as the initial result
        assert result_cached["source"] == "cache"

    def test_weather_service(self, weather_service):
        location = "New York"
        result = weather_service.get_weather_by_location(location)
        assert result["location"]["name"] == location

    def test_weather_service_invalid_location(self, weather_service):
        location = " "
        result = weather_service.get_weather_by_location(location)
        print(result)
        assert result is None

    def test_weather_service_api_key_missing(self, weather_service):
        weather_service.api_key = None
        location = "New York"
        # Clear the cache
        redis_client = redis.Redis()
        redis_client.delete(location)

        with pytest.raises(WeatherAPIKeyMissingError):
            weather_service.get_weather_by_location(location)
