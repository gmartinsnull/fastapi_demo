terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.81.0"
    }
  }

  backend "s3" {
    bucket = "fastapi-tfstate"
    key    = "state/terraform.tfstate"
    region = "us-west-2"
  }

  required_version = ">= 1.10.3"
}

provider "aws" {
  region = "us-west-2"
}

data "aws_vpc" "default" {
  default = true
}

data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }

  filter {
    name   = "default-for-az"
    values = ["true"]
  }
}

output "available_subnets" {
  value       = data.aws_subnets.default.ids
  description = "List of default subnet IDs in the default VPC"
}

resource "aws_security_group" "fastapi_sg" {
  name        = "fastapi-terraform-sg"
  vpc_id      = data.aws_vpc.default.id
  description = "Allow SSH and HTTP"

  # Allow SSH (port 22) from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow HTTP (port 80) from anywhere
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "ec2_public_ip" {
  value       = aws_instance.t2_micro.public_ip
  description = "The public IP address of the EC2 instance."
}


# Create an EC2 Instance
resource "aws_instance" "t2_micro" {
  ami                         = "ami-07d9cf938edb0739b"
  instance_type               = "t2.micro"
  key_name                    = "gmartins-macpro-2015"
  vpc_security_group_ids      = [aws_security_group.fastapi_sg.id]
  subnet_id                   = data.aws_subnets.default.ids[0]
  associate_public_ip_address = true

  root_block_device {
    volume_size = 8
    volume_type = "gp3"
  }

  tags = {
    Name = "FastAPI-Terraform-EC2"
  }
}
