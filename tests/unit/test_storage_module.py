def test_database_initialization(database_factory, sample_server, sample_network):
    db_name = "my-test-db"
    db_instance = database_factory(
        name=db_name,
        server=sample_server,
        network=sample_network
    )

    assert db_instance.name == db_name
    assert db_instance._depends_on == [sample_server, sample_network]
    assert db_instance.server == sample_server
    assert db_instance.network == sample_network
    assert db_instance.database_type is not None


def test_build(sample_database):
    result = sample_database.build()
    assert isinstance(result, list)
    assert len(result) == 1
    assert "null_resource" in result[0]
    assert "test-db" in result[0]["null_resource"]

    resource = result[0]["null_resource"]["test-db"]
    assert "local-exec" in resource["provisioner"]

    expected_command = f"echo 'Creando db {sample_database.name} con server {sample_database.server.name} y network {sample_database.network.name}'"
    assert resource["provisioner"]["local-exec"]["command"] == expected_command
