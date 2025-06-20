variable "name" {
  type    = string
  default = "server-1-us-east"
}

variable "network_name" {
  type = string
}

variable "instance_count" {
  type    = number
  default = 1

  validation {
    condition     = var.instance_count > 0
    error_message = "El numero de isntancias debe ser positivo"
  }
}

variable "region" {
  type    = string
  default = "us-east"
}
