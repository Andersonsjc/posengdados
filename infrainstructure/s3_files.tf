# File spark job for emr
resource "aws_s3_object" "job_spark" {
  bucket = aws_s3_bucket.dl.id #Referêrncia do datalake criado
  key    = "emr-code/pyspark/job_spark_from_tf.py"
  acl = "private"
  source = "../job_spark.py"          # Arquivo com o job spark que vai
  etag   = filemd5("../job_spark.py") # Define qual é o objeto de parâmetro
}