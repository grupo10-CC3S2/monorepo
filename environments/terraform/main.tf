module "network" {
  source = "../../modules/terraform/network_module"

  name = "network-1"
  port = 8080
}

module "compute" {
  source = "../../modules/terraform/compute_module"

  instance_count = 4
  name           = "server"
  network_name   = module.network.network_name_out

  depends_on = [module.network]
}

module "db" {
  source = "../../modules/terraform/storage_module"

  name           = "db-1"
  server_name    = module.compute.server_name_out
  network_name   = module.network.network_name_out
  size           = "3.5 TB"
  backup_enabled = true

  depends_on = [module.network, module.compute]
}
