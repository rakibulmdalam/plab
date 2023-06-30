import argparse
import logging
import multiprocessing as mp
from flask_restx import Api, apidoc
from waitress import serve
from flask import Flask
from flask_cors import CORS
import json

from configs.project_config import ProjectConfig
from utils import get_log_handler

# importing routes
from routes import shipments

# creating the Application Context
APP = Flask(__name__)
api = Api(
    APP, version="1.0", title="Track and Trace API", description="API documentation"
)

# adding namespaces
api.add_namespace(shipments.shipment_api)


# Custom route to generate and save the Swagger JSON file
@APP.route("/get_swagger")
def generate_swagger_json():
    swagger_data = api.__schema__
    with open("open_api.json", "w") as file:
        file.write(json.dumps(swagger_data))  # type: ignore
    return "Swagger JSON file generated"


# TODO: custom error handlers


@api.documentation
def custom_ui():
    return apidoc.ui_for(api)


def run():
    PARSER = argparse.ArgumentParser(description="Track and Trace API server")
    PARSER.add_argument("--port", type=int, help="Specify port number")
    PARSER.add_argument(
        "--debug",
        action="store_true",
        help="Use flask debug/dev mode with file change reloading",
    )
    ARGS = PARSER.parse_args()

    # create AppLogger from here
    logger = logging.getLogger(ProjectConfig().LOGGER_NAME)
    handler = get_log_handler()
    logger.addHandler(handler)
    logger.setLevel(ProjectConfig().LOG_LEVEL)
    logger.info("Logging initiated")

    if ARGS.debug:
        CORS(APP)
        try:
            logger.info("Running in debug mode")
            # running werkzeug's flask server instead of wsgi (waitress)
            PORT = ARGS.port if ARGS.port else ProjectConfig().PORT
            APP.run(host="0.0.0.0", port=PORT, debug=True)
        except KeyboardInterrupt:
            logger.info("Keyboard Interrupt. Stopping server.")
        except Exception as e:
            logger.info("Stopping server due to Exception: {}".format(e))
            raise e
        finally:
            logger.info("WSGI server stopped")
    else:
        try:
            # running wsgi (waitress) standard server
            logger.info("Running in production mode")
            num_workers = mp.cpu_count()
            serve(APP, port=ProjectConfig().PORT, threads=num_workers)
        except KeyboardInterrupt:
            logger.info("Keyboard Interrupt. Stopping server.")
        except Exception as e:
            logger.info("Stopping server due to Exception: {}".format(e))
            raise e
        finally:
            logger.info("WSGI server stopped")


if __name__ == "__main__":
    run()
