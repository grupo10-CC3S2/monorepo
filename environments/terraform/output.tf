output "info_completa" {
  description = "Info completa de la infraestructura"
  value = {
    network_info = module.network.network_info
    compute_info = module.compute.compute_info
    storage_info = module.db.storage_info
  }
}
