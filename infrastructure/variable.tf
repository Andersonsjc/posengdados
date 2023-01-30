variable "aws_region" {
  default = "us-east-1"
}

variable "base_bucket_name" {
  default = "datalake-igti-tf"
}

variable "ambiente" {
  default = "producao"
}

variable "numero_conta" {
  default = "511442505751"
}

variable "lambda_function_name" {
  default = "IGTIexecutaEMRaovivo"
}

variable "key_pair_name" {
  default = "anderson-igti-teste"
}

variable "airflow_subnet_id" {
  default = "subnet-003605a03dc6e126a"
}

variable "vpc_id" {
  default = "vpc-08b2e216b0d6e2fc2"
}