# Network outputs
output "vpc_id" {
  value = module.network.vpc_id
}

output "public_subnet_ids" {
  value = module.network.public_subnet_ids
}

# Compute outputs
output "ec2_instance_ids" {
  value = module.compute.instance_ids
}

output "ec2_public_ips" {
  value = module.compute.public_ips
}

# Storage outputs
output "s3_bucket_id" {
  value = module.storage.bucket_id
}

output "s3_bucket_arn" {
  value = module.storage.bucket_arn
}
