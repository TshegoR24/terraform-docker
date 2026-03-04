output "container_name" {
  description = "Name of the running container"
  value       = docker_container.nginx.name
}

output "container_port" {
  description = "Port the container is running on"
  value       = var.nginx_port
}