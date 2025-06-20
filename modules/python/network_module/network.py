class NetworkFacade:
    def __init__(self, network, name, port, region):
        self._network = network
        self._name = name
        self._port = port
        self._region = region


class NetworkFactoryModule:
    def __init__(self, name, port=80, region="us-east"):
        if not isinstance(port, int) or port <= 0 or port > 65535:
            raise ValueError("El puerto debe estar entre 1 y 65535")

        self.name = name
        self.port = port
        self.region = region
        self.network_name = f"{self.name}"

    def build(self):
        command = (
            f"echo 'Creando network {self.network_name} " f"con puerto {self.port} y region {self.region}'"
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

    def outputs(self):
        return NetworkFacade(
            network=self.network_name,
            name=self.name,
            port=self.port,
            region=self.region
        )
