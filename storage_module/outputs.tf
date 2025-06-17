output "db_name_out" {
  description = "El nombre de la db creada"
  value       = var.name
}

output "storage_path" {
  description = "Path de la db"
  value = "/db/${var.name}"
}