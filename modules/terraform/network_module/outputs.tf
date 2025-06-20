output "network_name_out" {
  description = "El nombre de la network creada"
  value       = var.name
}

output "network_info" {
  description = "Informacion de la network creada"
  value = {
    name    = var.name
    port    = var.port
    region  = var.region
    version = "v1.0.0"
  }
}
