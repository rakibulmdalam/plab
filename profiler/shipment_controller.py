import os
import sys

sys.path.append("configs/")
from project_config import ProjectConfig

path = ProjectConfig().PROJECT_DIR
exclude = [".git", "__pycache__", "node_modules", "ui", "js", "css", "data"]
DIRS = [x[0] for x in os.walk(path)]
for d in DIRS:
    split_d = d.split("/")
    common = list(set(split_d).intersection(exclude))
    if len(common) < 1:
        sys.path.append(d + "/")

from controllers.shipments import ShipmentController
from line_profiler import LineProfiler


def profile_shipment_controller():
    # Create an instance of ShipmentController
    shipment_controller = ShipmentController()

    # Create a LineProfiler object
    profiler = LineProfiler()

    # Add the track_shipment method to be profiled
    profiler.add_function(shipment_controller.track_shipment)

    # Run the profiling
    profiler.enable()
    params = {"tracking_number": "TN12345678"}
    shipment_controller.track_shipment(
        params
    )  # Call the method or execute your code here
    profiler.disable()

    # Print the profiling results
    profiler.print_stats()


if __name__ == "__main__":
    profile_shipment_controller()
