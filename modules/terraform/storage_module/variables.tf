variable "name" {
  type    = string
  default = "db-1-us-east"
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
  default = true
}

variable "region" {
  type    = string
  default = "us-east"
}
