files = {
    'main.tf': '''terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:alpine"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "terraform-nginx"

  ports {
    internal = 80
    external = 8090
  }
}''',

    'variables.tf': '''variable "nginx_port" {
  description = "External port for the nginx container"
  type        = number
  default     = 8090
}

variable "container_name" {
  description = "Name of the nginx container"
  type        = string
  default     = "terraform-nginx"
}''',

    'outputs.tf': '''output "container_name" {
  description = "Name of the running container"
  value       = docker_container.nginx.name
}

output "container_port" {
  description = "Port the container is running on"
  value       = var.nginx_port
}'''
}

for filename, content in files.items():
    with open(filename, 'w') as f:
        f.write(content)
    print(f'{filename} created successfully!')