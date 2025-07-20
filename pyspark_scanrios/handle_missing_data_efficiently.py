from pyspark.sql import SparkSession
from pyspark.sql.functions import col,mean

data = [ (1, "Laptop", 1000, 5), (2, "Mouse", None, None), (3, "Keyboard", 50, 2), (4, "Monitor", 200, None), (5, None, 500, None), ] 
columns = ["product_id", "product", "price", "quantity"]
df = spark.createDataFrame(data,columns)
display(df)
from pyspark.sql.functions import mean, col, when
mean_price = df.agg(mean(col("price"))).collect()[0][0]
print(mean_price)
df = df.withColumn("price", when(col("price").isNull(),mean_price).otherwise(col("price"))).withColumn("quantity",when(col("quantity").isNull(),1).otherwise(col("quantity")))
display(df)