import pytest


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


@pytest.mark.parametrize("name,instance_count,should_raise,error_msg", [
    ("server", 1, False, None),
    ("cien-server", 100, False, None),
    ("zero-server", 0, True, "El numero de instancias debe ser positivo"),
    ("negative-server", -1, True, "El numero de instancias debe ser positivo"),
    ("float-server", 2.5, True, "El numero de instancias debe ser positivo"),
    ("string-server", "4", True, "El numero de instancias debe ser positivo"),
])
def test_server_instance_count(server_factory, sample_network, name, instance_count, should_raise, error_msg):
    if should_raise:
        with pytest.raises(ValueError, match=error_msg):
            server_factory(name=name, network=sample_network, instance_count=instance_count)
    else:
        server_instance = server_factory(name=name, network=sample_network, instance_count=instance_count)
        assert server_instance.name == name
        assert server_instance.instance_count == instance_count
        assert server_instance.network == sample_network
