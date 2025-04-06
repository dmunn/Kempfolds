module "public_ecr" {
  source = "terraform-aws-modules/ecr/aws"

  # ECR resides solely within eu-east-1
  providers = {
    aws = aws.us-east-1
  }

  repository_name = "${terraform.workspace}-${var.project_name}"
  repository_type = "public"

  public_repository_catalog_data = {
    description       = "A container serving a flask site which loads a random kempfolds images"
    operating_systems = ["Linux"]
    architectures     = ["x86"]
  }

  tags = {
    "module" = "ecr"
  }
}
