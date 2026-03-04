variable "nginx_port" {
  description = "External port for the nginx container"
  type        = number
  default     = 8090
}

variable "container_name" {
  description = "Name of the nginx container"
  type        = string
  default     = "terraform-nginx"
}