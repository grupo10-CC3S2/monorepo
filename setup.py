import json
from network_module.network import NetworkFactoryModule
from compute_module.server import ServerFatoryModule
from storage_module.database import DatabaseFactoryModule

if __name__ == "__main__":
    network_name = "network-1"
    server_name = "server-1"
    db_name = "db-1"
    port = 8080
    network_factory = NetworkFactoryModule(network_name, port)
    server_factory = ServerFatoryModule(server_name, network_factory)
    database_factory = DatabaseFactoryModule(
        db_name, server_factory, network_factory
    )
    network_build = network_factory.build()
    server_build = server_factory.build()
    database_build = database_factory.build()
    resources = {"resource": network_build + server_build + database_build}

    with open("main.tf.json", "w") as f:
        json.dump(resources, f, indent=4)
