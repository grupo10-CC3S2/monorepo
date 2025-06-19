def test_server_initialization(server_factory, sample_network):
    server_name = "test-server"
    server_instance = server_factory(name=server_name, network=sample_network, instance_count=4)

    assert server_instance.name == server_name
    assert server_instance.network == sample_network
    assert sample_network in server_instance._depends_on


def test_build(sample_server):
    result = sample_server.build()

    assert isinstance(result, list)
    assert len(result) == 1

    assert "null_resource" in result[0]
    assert "test-server" in result[0]["null_resource"]

    resource = result[0]["null_resource"]["test-server"]
    assert "local-exec" in resource["provisioner"]

    assert resource["count"] == 4

    expected_command = f"echo 'Creando server {sample_server.name} con network {sample_server.network.name}'"
    assert resource["provisioner"]["local-exec"]["command"] == expected_command
