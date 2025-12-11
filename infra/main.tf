############################################
# NETWORK MODULE
############################################
module "network" {
  source = "./modules/network"

  project_name     = var.project_name
  vpc_cidr         = var.vpc_cidr
  vpc_name         = var.vpc_name           # optional, defaults to "my-vpc"
  public_subnets   = var.public_subnets
  private_subnets  = var.private_subnets
  azs              = var.azs
}


############################################
# COMPUTE MODULE
############################################
module "compute" {
  source = "./modules/compute"

  project_name   = var.project_name
  instance_count = var.instance_count
  ami_id         = var.ami_id
  instance_type  = var.instance_type
  subnet_ids     = module.network.public_subnet_ids
  key_name       = var.key_name
  instance_name  = var.instance_name
  tags           = var.tags
}


############################################
# STORAGE MODULE
############################################
module "storage" {
  source = "./modules/storage"

  bucket_name          = var.bucket_name
  versioning           = var.versioning
  enable_encryption    = var.enable_encryption
  encryption_algorithm = var.encryption_algorithm
  project_name         = var.project_name
}

