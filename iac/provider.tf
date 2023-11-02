provider "aws" {
    region = "us-east-1"
    access_key = "fake"
    secret_key = "fake"
    s3_force_path_style = true
    skip_credentials_validation = true
    skip_metadata_api_check = true
    skip_requesting_account_id = true

    endpoints {
      s3 = "http://localhost:4566"
    }

    default_tags {
      tags = {
        environment = "local"
        service = "local-stack"
      }
    }
}

terraform {
  required_version = ">= 1.1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.74"
    }
  }
}