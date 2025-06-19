def test_network_initialization(network_factory):
    network_name = "test-network"
    network_port = 8080

    network_instance = network_factory(
        name=network_name,
        port=network_port
    )

    assert network_instance.name == network_name
    assert network_instance.port == network_port
    assert not hasattr(network_instance, '_depends_on')


def test_build(sample_network):
    result = sample_network.build()
    assert isinstance(result, list)
    assert len(result) == 1

    assert "null_resource" in result[0]
    assert "test-network" in result[0]["null_resource"]

    resource = result[0]["null_resource"]["test-network"]
    assert "local-exec" in resource["provisioner"]

    expected_command = f"echo 'Creando network {sample_network.name}-us-east con puerto {sample_network.port}'"
    assert resource["provisioner"]["local-exec"]["command"] == expected_command
