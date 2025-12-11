variable "project_name" {
  type        = string
  description = "Name of the project for resource naming"
}
variable "instance_count" {
  description = "Number of EC2 instances to launch"
  type        = number
  default     = 1
}

variable "ami_id" {
  description = "AMI ID for the EC2 instances"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "subnet_ids" {
  description = "List of subnet IDs to launch instances in"
  type        = list(string)
}

variable "key_name" {
  description = "EC2 Key pair name for SSH access"
  type        = string
}

variable "instance_name" {
  description = "Base name for the instances"
  type        = string
  default     = "compute-instance"
}

variable "tags" {
  description = "Additional tags to add to the instances"
  type        = map(string)
  default     = {}
}
