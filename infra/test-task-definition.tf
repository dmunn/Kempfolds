resource "aws_ecs_task_definition" "task_definition" {
  family                   = var.project_name
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  execution_role_arn       = "arn:aws:iam::518035887622:role/ecsTaskExecutionRole"
  container_definitions    = file("files/task-definition.json")
  cpu                      = 256
  memory                   = 512
}
