provider "aws" {
  region = var.aws_region
}

#Centralizar o arquivo de controle de estado do terraform
terraform {
  backend "s3" {
    buket = "terraform-anderson-igti-edc"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-1"
  }
}
