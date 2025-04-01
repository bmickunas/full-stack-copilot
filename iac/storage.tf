resource "aws_dynamodb_table" "things" {
  name           = "things"
  hash_key       = "id"
  billing_mode   = "PAY_PER_REQUEST"

  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "created_at"
    type = "S"
  }

  attribute {
    name = "modified_at"
    type = "S"
  }
}