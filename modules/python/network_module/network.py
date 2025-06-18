class NetworkFactoryModule:
    def __init__(self, name, port):
        self.name = name
        self.port = port
        self.network_name = f"{self.name}-us-east"

    def build(self):
        command = (
            f"echo 'Creando network {self.network_name} " f"con puerto {self.port}'"
        )

        return [
            {
                "null_resource": {
                    self.name: {
                        "provisioner": {"local-exec": {"command": command}},
                    },
                }
            }
        ]
