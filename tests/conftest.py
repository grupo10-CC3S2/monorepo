from modules.python.network_module.network import NetworkFactoryModule
from modules.python.compute_module.server import ServerFactoryModule
from modules.python.storage_module.database import DatabaseFactoryModule
import pytest


@pytest.fixture
def sample_network():
    return NetworkFactoryModule("test-network", 8080)


@pytest.fixture
def sample_network_custom():
    return NetworkFactoryModule("test-net", 443)


@pytest.fixture
def sample_server(sample_network):
    return ServerFactoryModule("test-server", sample_network, 4)


@pytest.fixture
def sample_database(sample_server, sample_network):
    return DatabaseFactoryModule("test-db", sample_server, sample_network)


@pytest.fixture
def network_factory():
    return NetworkFactoryModule


@pytest.fixture
def server_factory():
    return ServerFactoryModule


@pytest.fixture
def database_factory():
    return DatabaseFactoryModule
