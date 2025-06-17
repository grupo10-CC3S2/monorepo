resource "null_resource" "server-1" {
  count = var.instance_count

  provisioner "local-exec" {
    command = "echo 'Creando server ${var.name} con network ${var.network_name}'"
  }
}
