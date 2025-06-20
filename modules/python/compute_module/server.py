class ServerFactoryModule:
    def __init__(self, name, network, instance_count=1):
        if not isinstance(instance_count, int) or instance_count <= 0:
            raise ValueError("El numero de instancias debe ser positivo")

        self.name = name
        self.network = network
        self.server_type = "web"
        self.instance_count = instance_count
        self._depends_on = [self.network]

    def build(self):
        command = f"echo 'Creando server {self.name} con network {self.network.name}'"

        return [
            {
                "null_resource": {
                    self.name: {
                        "count": self.instance_count,
                        "provisioner": {"local-exec": {"command": command}},
                        "depends_on": [f"null_resource.{dep.name}" for dep in self._depends_on],
                    },
                }
            }
        ]
