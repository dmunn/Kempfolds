# README

## Dependencies
- A session with an IAM role to enable terraform to deploy the resources defined within
- An S3 Bucket called "kempfoldsinfra"

## Usage
- Initialise terraform: `make init`
- Plan for the development account: `make plan-dev`
- Plan for the production account: `make plan-prd`

## Bootstrap
- Deploy infra
    - Take note of ECR_URI output
- Push image to repo
    - Login into docker: `aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ECR_URI - minus the last forward slash and repo name>`
    - Build the image, supporting x86_64 arch: `docker buildx build --platform linux/amd64 -t kempfolds .`
    - Tag the image: `docker tag kempfolds:latest <ECR_URI>:latest`
    - Push the image to the repo: `docker push <ECR_URI>:latest`
- Wait for new container to be started within ECS
- Grab the "ALB_URL" and terraform output and enter it into your browser of choice, accept the HTTPS warning and proceed.

## Development
If you would like to create different settings for the environments, mapped to different accounts then please override the existing variables found within the `variables.tf` file by adding a new value within the correct environment specific variable file, found within the `vars/{environment}.tfvars` directory.

**Note:** There are no overridden values in these environment specific files as the configuration is designed, currently, for parity regardless of environment / account.

## Deploying to multiple AWS accounts
There are multiple ways to achieve this:
1. Localised Deployment (Assume Role using IAM User credentials):
    1. Log into the account you want to target by using `aws sso login`
    2. Select your account
    3. Export the profile that was outputted from the command above: `export AWS_PROFILE=<INSERT PROFILE NAME>`
    4. Initialise Terraform: `make init`
    5. Select environment, mapped to account (example): `make plan-prd`
    6. Deploy: `make apply`
2. CI/CD (Assume Role directly using GitHub OIDC provider):
    1. TBA: See "TODO" section below

## TODO
- Add HTTPS support
- Update Makefile to conditionally create workspace if it doesn't exist
- Update Makefile to bootstrap state bucket
- Implement CI/CD pipeline for changes
    - Use Github Actions, see [conigure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials) as a starting point to understand auth requirements.