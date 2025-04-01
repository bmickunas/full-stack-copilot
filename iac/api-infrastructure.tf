resource "aws_api_gateway_rest_api" "things_api" {
  name        = "things_api"
  description = "API for managing things"
}

resource "aws_api_gateway_resource" "things" {
  rest_api_id = aws_api_gateway_rest_api.things_api.id
  parent_id   = aws_api_gateway_rest_api.things_api.root_resource_id
  path_part   = "things"
}

resource "aws_api_gateway_method" "create_thing" {
  rest_api_id   = aws_api_gateway_rest_api.things_api.id
  resource_id   = aws_api_gateway_resource.things.id
  http_method   = "POST"
  authorization = "AWS_IAM"
}

resource "aws_api_gateway_method" "read_thing" {
  rest_api_id   = aws_api_gateway_rest_api.things_api.id
  resource_id   = aws_api_gateway_resource.things.id
  http_method   = "GET"
  authorization = "AWS_IAM"
}