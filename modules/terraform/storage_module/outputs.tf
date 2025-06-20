output "db_name_out" {
  description = "El nombre de la db creada"
  value       = var.name
}

output "storage_path" {
  description = "Path de la db"
  value       = "/db/${var.name}"
}

output "backup_path" {
  description = "Path del backup de la db"
  value       = "./backup/${var.name}"
}

output "storage_info" {
  description = "Informacion de la db creada"
  value = {
    name           = var.name
    network_name   = var.network_name
    server_name    = var.server_name
    size           = var.size
    backup_enabled = var.backup_enabled
    region         = var.region
    version        = "v1.0.0"
  }
  depends_on = [var.network_name, var.server_name]
}
