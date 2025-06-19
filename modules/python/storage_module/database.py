class DatabaseFactoryModule:
    def __init__(self, name, server, network):
        self.name = name
        self.server = server
        self.network = network
        self.database_type = "sqlite"

    def build(self):
        command = f"echo 'Creando db {self.name} con server {self.server.name} y network {self.network.name}'"

        return [
            {
                "null_resource": {
                    self.name: {
                        "provisioner": {"local-exec": {"command": command}},
                    },
                }
            }
        ]
