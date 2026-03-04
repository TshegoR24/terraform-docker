# Terraform Docker Infrastructure

Infrastructure as Code (IaC) project using Terraform to provision and manage Docker containers locally.

## What I learned
- Writing Terraform configuration files
- Using variables and outputs in Terraform
- The terraform init → plan → apply workflow
- Managing infrastructure as code

## Project Structure
- `main.tf` - Main infrastructure configuration
- `variables.tf` - Input variables
- `outputs.tf` - Output values

## How to run

### Prerequisites
- Terraform installed
- Docker Desktop running

### Steps
```bash
terraform init
terraform plan
terraform apply
```

Then visit http://localhost:8090

## Tech Stack
- Terraform
- Docker
- Nginx