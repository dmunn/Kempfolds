module "ecs_cluster" {
  source = "terraform-aws-modules/ecs/aws//modules/cluster"

  cluster_name = "${terraform.workspace}-${var.project_name}"

  cluster_configuration = {
    execute_command_configuration = {
      logging = "OVERRIDE"
      log_configuration = {
        cloud_watch_log_group_name = "/aws/ecs/${terraform.workspace}-${var.project_name}"
      }
    }
  }

  fargate_capacity_providers = {
    FARGATE = {
      default_capacity_provider_strategy = {
        weight = 50
      }
    }
    FARGATE_SPOT = {
      default_capacity_provider_strategy = {
        weight = 50
      }
    }
  }

  tags = {
    "module" = "ecs_cluster"
  }
}

resource "aws_alb" "application_load_balancer" {
  name               = "${terraform.workspace}-${var.project_name}"
  internal           = false
  load_balancer_type = "application"
  subnets            = module.vpc.public_subnets
  security_groups    = [module.ecs_service.security_group_id]
}

resource "aws_lb_target_group" "target_group" {
  name        = "${terraform.workspace}-${var.project_name}"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = module.vpc.vpc_id
}

resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_alb.application_load_balancer.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target_group.arn
  }
}

module "ecs_service" {
  source = "terraform-aws-modules/ecs/aws//modules/service"

  name        = "${terraform.workspace}-${var.project_name}"
  cluster_arn = module.ecs_cluster.arn

  assign_public_ip = true

  requires_compatibilities = ["FARGATE"]

  cpu    = 1024
  memory = 4096

  # Create task definition file seperately to allow for continuous deployment using automation
  create_task_definition    = false
  task_definition_arn       = aws_ecs_task_definition.task_definition.arn
  create_task_exec_iam_role = true
  create_task_exec_policy   = true
  create_tasks_iam_role     = true

  load_balancer = {
    service = {
      target_group_arn = aws_lb_target_group.target_group.arn
      container_name   = "${var.project_name}"
      container_port   = 80
    }
  }

  subnet_ids = module.vpc.public_subnets
  security_group_rules = {
    alb_ingress_client = {
      type        = "ingress"
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      description = "Clients accessing site"
      cidr_blocks = [var.client_ip]
    }
    alb_ingress_vpc = {
      type        = "ingress"
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      description = "Internal AWS resources"
      cidr_blocks = [var.vpc_cidr]
    }
    egress_all = {
      type        = "egress"
      from_port   = 0
      to_port     = 0
      protocol    = "-1"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  tags = {
    "module" = "ecs_service"
  }
}
