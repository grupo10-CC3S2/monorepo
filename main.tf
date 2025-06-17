module "network" {
  source = "./network_module"

  name = "network-1"
  port = 8080
}

module "compute" {
  source = "./compute_module"

  instance_count = 4
  name           = "server-1"
  network_name   = module.network.network_name_out

  depends_on = [module.network]
}

module "db" {
  source = "./storage_module"

  name         = "db-1"
  server_name  = module.compute.server_name_out
  network_name = module.network.network_name_out

  depends_on = [module.network, module.compute]
}
