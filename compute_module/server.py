class ServerFatoryModule:
    def __init__(self, name, network, instance_count=1):
        self.name = name
        self.network = network
        self.server_type = "web"
        self.instance_count = instance_count

    def build(self):
        command = f"echo 'Creando server {self.name} con network {self.network.name}'"

        return [
            {
                "null_resource": {
                    self.name: {
                        "count": self.instance_count,
                        "provisioner": {"local-exec": {"command": command}},
                    },
                }
            }
        ]
