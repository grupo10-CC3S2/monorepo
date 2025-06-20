import pytest


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

    expected_command = f"echo 'Creando network {sample_network.name} con puerto {sample_network.port} y region us-east'"
    assert resource["provisioner"]["local-exec"]["command"] == expected_command


@pytest.mark.parametrize("name,port,region,should_raise,error_msg", [
    ("network", 80, None, False, None),
    ("prod-network", 443, "us-east", False, None),
    ("one-network", 1, None, False, None),
    ("max-port-network", 65535, "us-east", False, None),
    ("wrong-network", 0, "us-east", True, "El puerto debe estar entre 1 y 65535"),
    ("negative-network", -1, None, True, "El puerto debe estar entre 1 y 65535"),
    ("post-network", 100_000, "us-east", True, "El puerto debe estar entre 1 y 65535"),
    ("float-network", 2.5, None, True, "El puerto debe estar entre 1 y 65535"),
    ("string-network", "8080", None, True, "El puerto debe estar entre 1 y 65535"),
])
def test_network_ports(network_factory, name, port, region, should_raise, error_msg):
    if should_raise:
        with pytest.raises(ValueError, match=error_msg):
            network_factory(name=name, port=port, region=region)
    else:
        network_instance = network_factory(name=name, port=port, region=region)
        assert network_instance.name == name
        assert network_instance.port == port
        assert network_instance.region == region
