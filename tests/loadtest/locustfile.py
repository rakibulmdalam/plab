from locust import HttpUser, task, between, constant

class MyUser(HttpUser):
    wait_time = constant(0.001)  # Wait time between requests
    host = "http://localhost:5000"  # Set the target host

    @task
    def access_endpoint(self):
        self.client.get("/api/track/TN12345678")  # Make GET requests to your Flask endpoints

