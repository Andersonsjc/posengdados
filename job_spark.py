# comentario para notificiar o arquivo .py
import pyspark
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
          SparkSession.builder
                      .appName('tarn-csv-to-parquet')
                      .getOrCreate()
         )


enem = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("sep", ";")
    .option("encoding", "ISO-8859-1")
    .option("inferSchema", True)
    .load("s3://datalake-andersonjosesiqueira-511442505751/raw-data/enem/year-2020/MICRODADOS_ENEM_2020.bz2")
)

(
    enem
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-andersonjosesiqueira-511442505751/consumer-zone/enem/")
)