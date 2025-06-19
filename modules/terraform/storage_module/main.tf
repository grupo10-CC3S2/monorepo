resource "null_resource" "db-1" {
  triggers = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "echo 'Creando database ${var.name} con server ${var.server_name} con network ${var.network_name}'"
  }

  provisioner "local-exec" {
    command = var.backup_enabled ? "bash '${path.module}/backup_storage.sh' '${var.name}' 'full'" : "echo 'Sin backup para la db ${var.name}'"
  }
}
