class DatabaseFactoryModule:
    def __init__(self, name, server, network):
        self.name = name
        self.server = server
        self.network = network
        self.database_type = "sqlite"
        self._depends_on = [self.server, self.network]

    def build(self):
        command = f"echo 'Creando db {self.name} con server {self.server.name} y network {self.network.name}'"

        return [
            {
                "null_resource": {
                    self.name: {
                        "provisioner": {"local-exec": {"command": command}},
                        "depends_on": [f"null_resource.{dep.name}" for dep in self._depends_on],
                    },
                }
            }
        ]
