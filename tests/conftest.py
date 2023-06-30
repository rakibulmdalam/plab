import os
import sys

sys.path.append("configs/")

from project_config import ProjectConfig


def pytest_configure(config):
    print("-----------setup-----------")
    # register custom markers to avoid warnings
    markers = ["cardiocomm", "dbservice"]
    for marker in markers:
        config.addinivalue_line("markers", marker)

    path = ProjectConfig().PROJECT_DIR
    exclude = [".git", "__pycache__", "node_modules", "ui", "js", "css", "data"]
    DIRS = [x[0] for x in os.walk(path)]
    for d in DIRS:
        split_d = d.split("/")
        common = list(set(split_d).intersection(exclude))
        if len(common) < 1:
            sys.path.append(d + "/")


def pytest_unconfigure(config):
    # from sqlitemanager import SQLiteManager
    # TODO delete tables sometime before testing
    print("-----------teardown-----------")
    # sm = SQLiteManager()
    # conn = sm.connect()
    # c = conn.cursor()

    # sql = "DROP TABLE IF EXISTS checkins"
    # c.execute(sql)

    # sql = "DROP TABLE IF EXISTS transportboxes"
    # c.execute(sql)

    # conn.commit()
    # conn.close()
