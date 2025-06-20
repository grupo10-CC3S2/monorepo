variable "name" {
  type    = string
  default = "network-1"
}

variable "port" {
  type    = number
  default = 8080

  validation {
    condition     = var.port > 0 && var.port <= 65535
    error_message = "El puerto debe estar entre 1 y 65535"
  }
}

variable "region" {
  type    = string
  default = "us-east"
}
