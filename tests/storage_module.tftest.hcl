run "test_storage_init" {
  command = plan

  module {
    source = "./modules/terraform/storage_module"
  }

  variables {
    name           = "test-db"
    network_name   = "test-network"
    server_name    = "test-server"
    size           = "0.5 TB"
    backup_enabled = false
    region         = "us-east"
  }

  assert {
    condition     = output.db_name_out == "test-db"
    error_message = "El nombre de db en output debe coincidir con el nombre de entrada"
  }

  assert {
    condition     = output.storage_info.name == "test-db"
    error_message = "El nombre de la info de db en la info output debe coincidir con la entrada"
  }

  assert {
    condition     = output.storage_info.backup_enabled == false
    error_message = "El valor de backup_enabled en la info de db output debe ser false"
  }
}


run "test_storage_dependencies" {
  command = plan

  module {
    source = "./modules/terraform/storage_module"
  }

  variables {
    name         = "db"
    network_name = "network"
    server_name  = "server"
    region       = "us-east"
  }

  assert {
    condition     = output.storage_path == "/db/db"
    error_message = "El nombre de db en output debe coincidir con el nombre de entrada"
  }

  assert {
    condition     = output.storage_info.network_name == "network"
    error_message = "El nombre de network en info output debe ser el mismo que el de entrada de dependencia"
  }

  assert {
    condition     = output.storage_info.server_name == "server"
    error_message = "El nombre de server en info output debe ser el mismo que el de entrada de dependencia"
  }
}
