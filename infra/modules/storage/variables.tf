variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}



variable "versioning" {
  description = "Enable versioning for the bucket"
  type        = bool
  default     = true
}

variable "enable_encryption" {
  description = "Enable server-side encryption"
  type        = bool
  default     = true
}

variable "encryption_algorithm" {
  description = "Server-side encryption algorithm"
  type        = string
  default     = "AES256"
}

variable "tags" {
  description = "Additional tags for the bucket"
  type        = map(string)
  default     = {}
}

variable "project_name" {
  description = "Project name used for tagging"
  type        = string
}
