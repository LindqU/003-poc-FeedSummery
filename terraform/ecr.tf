################################################################################
# ECR                                                                          #
################################################################################
resource "aws_ecr_repository" "getemployee" {
  name = local.ecr_getemployee_repository_name
}

data "aws_ecr_authorization_token" "token" {}

resource "null_resource" "image_push" {
  provisioner "local-exec" {
    command = <<-EOF
      docker build ../ -t ${aws_ecr_repository.getemployee.repository_url}:latest; \
      docker login -u AWS -p ${data.aws_ecr_authorization_token.token.password} ${data.aws_ecr_authorization_token.token.proxy_endpoint}; \
      docker push ${aws_ecr_repository.getemployee.repository_url}:latest
    EOF
  }
}
