run "test_network_init" {
  command = plan

  module {
    source = "./modules/terraform/network_module"
  }

  variables {
    name   = "test-network"
    port   = 8080
    region = "us-east"
  }

  assert {
    condition     = output.network_name_out == "test-network"
    error_message = "El nombre de la red de output debe coincidir con la variable de entrada"
  }

  assert {
    condition     = output.network_info.port == 8080
    error_message = "El puerto de la información de la red debe coincidir con la entrada"
  }
}

run "test_network_custom_data" {
  command = plan

  module {
    source = "./modules/terraform/network_module"
  }

  variables {
    name   = "custom-network"
    port   = 443
    region = "us-west"
  }

  assert {
    condition     = output.network_info.port == 443
    error_message = "El puerto de la red debe ser 443"
  }

  assert {
    condition     = output.network_info.region == "us-west"
    error_message = "La red debe usar la region us-west"
  }
}

run "test_network_ports" {
  command = plan

  module {
    source = "./modules/terraform/network_module"
  }

  variables {
    name   = "network"
    port   = 100000
    region = "us-east"
  }

  expect_failures = [var.port]
}
