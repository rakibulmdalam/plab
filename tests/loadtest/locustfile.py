from locust import HttpUser, task, constant
import sys

sys.path.append("configs/")
from namespace_config import NamespaceConfig


class MyUser(HttpUser):
    wait_time = constant(0.001)  # Wait time between requests
    host = "http://localhost:5000"  # Set the target host

    @task
    def access_endpoint(self):
        # using the namespace config to get the path when running the load test within the project folder
        # otherwise, you can use the endpoint path directly. e.g. /api/v1/shipments/track/TN12345678
        url = NamespaceConfig().SHIPMENTS_PATH + "/track/TN12345678"
        self.client.get(url)  # Make GET requests to your Flask endpoints
