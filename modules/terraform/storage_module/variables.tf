variable "name" {
  type    = string
  default = "db"
}

variable "network_name" {
  type = string
}

variable "server_name" {
  type = string
}

variable "size" {
  type    = string
  default = "2 TB"
}

variable "backup_enabled" {
  type    = bool
  default = false
}

variable "region" {
  type    = string
  default = "us-east"
}
