# HCL - Hardshicop Configuration Language
# Linguagem declarativa


resource "aws_s3_bucket" "dl" {
    # Parâmetros de configuração do recurso escolhido
    bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}" #"datalake-andersonjosesiqueira-511442505751"
    acl = "private"
    tags = {
        IES   = "IGTI"
        CURSO = "EDC"
    }

    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }
}