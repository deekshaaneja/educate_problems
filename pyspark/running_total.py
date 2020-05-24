from pyspark import SparkConf, SparkContext, SQLContext
import pyspark.sql.functions as F
import os
from pyspark.sql.window import Window

conf = SparkConf().set("spark.driver.host", "127.0.0.1").set("spark.sql.shuffle.partitions", "8")
sc = SparkContext(master="local[*]", appName="Running Total", conf=conf)
sqlcontext = SQLContext(sc)

folder_path = os.path.join(os.getcwd(), "pyspark", "input_data")
PATH = os.path.join(folder_path, 'running_total_data.csv')


def find_running_sum():
    df = sqlcontext.read.option("multiline", "true") \
                .option("header", "true") \
                .csv(PATH)
    wind = Window.orderBy("id")
    wind_col = F.sum(F.col("orderQty")).over(wind)
    df_running_total = df.select("*", wind_col.alias("running_total")) \
                        .show()

if __name__ == "__main__":
    find_running_sum()