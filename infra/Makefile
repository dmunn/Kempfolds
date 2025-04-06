init:
	terraform init

plan-dev:
	terraform workspace select dev
	terraform fmt
	terraform validate
	terraform plan -var-file=vars/dev.tfvars

plan-prd:
	terraform workspace select prd
	terraform fmt
	terraform validate
	terraform plan -var-file=vars/prd.tfvars

apply:
	terraform apply -auto-approve

destroy:
	terraform apply -destroy