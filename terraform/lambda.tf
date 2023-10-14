################################################################################
# Lambda                                                                       #
################################################################################
resource "aws_lambda_function" "getemployee" {
  depends_on = [
    aws_cloudwatch_log_group.lambda_getemployee,
    null_resource.image_push,
  ]

  function_name = local.lambda_getemployee_function_name
  package_type  = "Image"
  image_uri     = "${aws_ecr_repository.getemployee.repository_url}:latest"
  role          = aws_iam_role.lambda_getemployee.arn
  publish       = true

  memory_size = 128
  timeout     = 28

  lifecycle {
    ignore_changes = [
      image_uri, last_modified
    ]
  }
}

################################################################################
# IAM Role for Lambda                                                          #
################################################################################
resource "aws_iam_role" "lambda_getemployee" {
  name               = local.lambda_getemployee_iam_role_name
  assume_role_policy = data.aws_iam_policy_document.lambda_getemployee_assume.json
}

data "aws_iam_policy_document" "lambda_getemployee_assume" {
  statement {
    effect = "Allow"

    actions = [
      "sts:AssumeRole",
    ]

    principals {
      type = "Service"
      identifiers = [
        "lambda.amazonaws.com",
      ]
    }
  }
}

resource "aws_iam_role_policy_attachment" "lambda_getemployee" {
  role       = aws_iam_role.lambda_getemployee.name
  policy_arn = aws_iam_policy.lambda_getemployee_custom.arn
}

resource "aws_iam_policy" "lambda_getemployee_custom" {
  name   = local.lambda_getemployee_iam_policy_name
  policy = data.aws_iam_policy_document.lambda_getemployee_custom.json
}

data "aws_iam_policy_document" "lambda_getemployee_custom" {
  statement {
    effect = "Allow"

    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents",
    ]

    resources = [
      "*",
    ]
  }
}

################################################################################
# CloudWatch Logs                                                              #
################################################################################
resource "aws_cloudwatch_log_group" "lambda_getemployee" {
  name              = "/aws/lambda/${local.lambda_getemployee_function_name}"
  retention_in_days = 3
}

################################################################################
# Lambda Alias                                                                 #
################################################################################
resource "aws_lambda_alias" "getemployee_prod" {
  name             = "Prod"
  function_name    = aws_lambda_function.getemployee.arn
  function_version = aws_lambda_function.getemployee.version

  lifecycle {
    ignore_changes = [function_version]
  }
}

################################################################################
# Lambda Permission                                                            #
################################################################################
resource "aws_lambda_permission" "allow_apigateway" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.getemployee.function_name
  principal     = "apigateway.amazonaws.com"
  qualifier     = aws_lambda_alias.getemployee_prod.name
}
