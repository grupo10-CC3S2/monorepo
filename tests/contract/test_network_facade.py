from modules.python.network_module.network import NetworkFactoryModule, NetworkFacade
import pytest

network_name = 'hello-world'
network_port = 8080
network_region = 'us-west'


@pytest.fixture
def network_outputs():
    network = NetworkFactoryModule(
        name=network_name,
        port=network_port,
        region=network_region
    )
    return network.outputs()


def test_network_output_is_facade(network_outputs):
    assert isinstance(network_outputs, NetworkFacade)


def test_network_output_has_network_name(network_outputs):
    assert network_outputs._network == f"{network_name}"


def test_network_output_has_port_and_region(network_outputs):
    assert network_outputs._port == network_port
    assert network_outputs._region == network_region


@pytest.mark.parametrize("name,port,region", [
    ("prod-network", 443, "us-east"),
    ("dev-network", 8080, "us-west"),
    ("test-network", 3000, "brazil"),
    ("network12345", 9000, "peru")
])
def test_network_facade_parametrized(name, port, region):
    network = NetworkFactoryModule(name=name, port=port, region=region)
    outputs = network.outputs()

    assert isinstance(outputs, NetworkFacade)
    assert outputs._network == name
    assert outputs._port == port
    assert outputs._region == region
