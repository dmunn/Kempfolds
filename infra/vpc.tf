module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  name = "${terraform.workspace}-${var.project_name}"
  cidr = var.vpc_cidr

  azs             = ["eu-west-1a", "eu-west-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  enable_nat_gateway     = true
  single_nat_gateway     = false
  one_nat_gateway_per_az = true

  manage_default_security_group = false

  tags = {
    "module" = "vpc"
  }
}
