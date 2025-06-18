resource "null_resource" "db-1" {
  provisioner "local-exec" {
    command = "echo 'Creando database ${var.name} con server ${var.server_name} con network ${var.network_name}'"
  }
}
