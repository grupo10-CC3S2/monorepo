resource "null_resource" "server-1" {
  count = var.instance_count

  provisioner "local-exec" {
    command = "echo 'Creando server ${var.name} con network ${var.network_name}'"
  }

  provisioner "local-exec" {
    command = "python3 '${path.module}/compute_tool.py' '${var.name}_${count.index + 1}' '${var.network_name}' '${count.index + 1}' '${var.region}'"
  }
}
