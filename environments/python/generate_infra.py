import json
import sys

from pathlib import Path

PROJECT_ROOT = Path(__file__).parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from modules.python.network_module.network import NetworkFactoryModule  # noqa
from modules.python.compute_module.server import ServerFactoryModule    # noqa
from modules.python.storage_module.database import DatabaseFactoryModule    # noqa


if __name__ == "__main__":
    network_name = "network-1"
    server_name = "server-1"
    db_name = "db-1"
    port = 8080
    network_factory = NetworkFactoryModule(network_name, port)
    server_factory = ServerFactoryModule(server_name, network_factory)
    database_factory = DatabaseFactoryModule(
        db_name, server_factory, network_factory
    )
    network_build = network_factory.build()
    server_build = server_factory.build()
    database_build = database_factory.build()
    resources = {"resource": network_build + server_build + database_build}
    print("Generando recursos:")
    print(json.dumps(resources, indent=4, separators=(',', ': ')))

    with open("main.tf.json", "w") as f:
        json.dump(resources, f, indent=4)
