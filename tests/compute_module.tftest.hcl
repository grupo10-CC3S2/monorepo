run "test_compute_init" {
  command = plan

  module {
    source = "./modules/terraform/compute_module"
  }

  variables {
    name           = "test-server"
    network_name   = "test-network"
    instance_count = 2
    region         = "us-east"
  }

  assert {
    condition     = output.server_name_out == "test-server"
    error_message = "El nombre de output de server debe  coincidir con la variable input"
  }

  assert {
    condition     = output.compute_info[0].name == "test-server-1"
    error_message = "La primera instancia de server debe tener el nombre con su indice"
  }
}

run "test_compute_multiple_instances" {
  command = plan

  module {
    source = "./modules/terraform/compute_module"
  }

  variables {
    name           = "multi-server"
    network_name   = "network"
    instance_count = 5
    region         = "us-west"
  }

  assert {
    condition     = length(output.compute_info) == 5
    error_message = "Deberia crear exactamente 5 instancias de server"
  }

  assert {
    condition     = output.compute_info[4].name == "multi-server-5"
    error_message = "Last server instance should have correct indexed name"
  }
}

run "test_server_instance_count_invalid" {
  command = plan

  module {
    source = "./modules/terraform/compute_module"
  }

  variables {
    name           = "server"
    network_name   = "network"
    instance_count = -12
    region         = "us-east"
  }

  expect_failures = [var.instance_count]
}
