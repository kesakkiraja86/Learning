from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

def get_data():
    return spark.sql("""
        SELECT product,
               SUM(amount) sales
        FROM sales_demo
        GROUP BY product
    """).toPandas()