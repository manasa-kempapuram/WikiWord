#########################
# Global
#########################

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name prefix for all resources"
  type        = string
  default     = "wiki-word"
}

#########################
# Network module
#########################

variable "vpc_cidr" {
  description = "CIDR for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnets" {
  description = "Public subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.1.0/24"]
}

variable "private_subnets" {
  description = "Private subnet CIDR blocks"
  type        = list(string)
  default     = ["10.0.2.0/24"]
}

variable "azs" {
  description = "Availability zones"
  type        = list(string)
  default     = ["us-east-1a"]
}

#########################
# Compute module
#########################

variable "instance_count" {
  type        = number
  default     = 1
}

variable "ami_id" {
  type = string
}

variable "instance_type" {
  type    = string
  default = "t3.micro"
}

variable "key_name" {
  type = string
}

variable "instance_name" {
  type    = string
  default = "compute-instance"
}

variable "tags" {
  type = map(string)
  default = {
    project = "wiki-word"
  }
}

#########################
# Storage module
#########################

variable "bucket_name" {
  type = string
}

variable "versioning" {
  type    = bool
  default = true
}

variable "enable_encryption" {
  type    = bool
  default = true
}

variable "encryption_algorithm" {
  type    = string
  default = "AES256"
}
variable "vpc_name" {
  description = "Name tag for the VPC"
  type        = string
  default     = "my-vpc"
}

