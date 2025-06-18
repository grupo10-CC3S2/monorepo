resource "null_resource" "network-1" {
  provisioner "local-exec" {
    command = "echo 'Creando network ${var.name} con puerto ${var.port}'"
  }
}
