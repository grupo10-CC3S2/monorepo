output "server_name_out" {
  description = "El nombre del server creado"
  value       = var.name
}

output "compute_info" {
  description = "Informacion de servidores creado"
  value = [
    for i in range(var.instance_count) : {
      name         = "${var.name}-${i + 1}"
      region       = var.region
      network_name = var.network_name
      index_count  = i + 1
      version      = "v1.0.0"
    }
  ]
  depends_on = [var.network_name]
}
