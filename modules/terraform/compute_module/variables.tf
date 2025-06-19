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
}

variable "region" {
  type    = string
  default = "us-east"
}
