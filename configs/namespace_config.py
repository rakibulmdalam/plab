from dataclasses import dataclass


@dataclass
class NamespaceConfig:
    URL_PREFIX: str = ""  # "/api/v1"
    SHIPMENTS_PATH: str = URL_PREFIX + "/shipments"
