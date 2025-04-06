# TODO: Create kempfoldsInfra bucket then delete this - it's a bootstrap resource

module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "${terraform.workspace}-${var.project_name}"
  acl    = "private"

  control_object_ownership = true
  object_ownership         = "ObjectWriter"

  versioning = {
    enabled = true
  }

  tags = {
    "module" = "s3"
  }
}
