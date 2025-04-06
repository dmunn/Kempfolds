terraform {
  backend "s3" {
    bucket       = "kempfoldsinfra"
    key          = "state"
    region       = "eu-west-1"
    use_lockfile = "true"
  }
}