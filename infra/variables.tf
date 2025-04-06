variable "project_name" {
  type        = string
  description = "Single word to describe project - to be used for all resources"
  default     = "kempolds"
}

variable "vpc_cidr" {
  type        = string
  description = "The network range for the VPC that will be created"
  default     = "10.0.0.0/16"
}

variable "client_ip" {
  type        = string
  description = "The IP allowed to request the site"
  default     = "195.213.39.63/32"
}
