output "ECR_URI" {
  description = "Required for pushing images to the repo"
  value       = module.public_ecr.repository_url
}

output "ALB_URL" {
  description = "DNS or ALB so that you can visit the site"
  value       = aws_alb.application_load_balancer.dns_name
}
