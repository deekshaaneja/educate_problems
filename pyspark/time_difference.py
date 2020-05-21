from pyspark import SparkConf, SparkContext, SQLContext
import pyspark.sql.functions as F
from pyspark.sql.types import ArrayType, IntegerType
import os
import sys

conf = SparkConf().set("spark.driver.host", "127.0.0.1").set("spark.sql.crossJoin.enabled", "true") \
    .set("spark.sql.shuffle.partitions", "8")
sc = SparkContext(master='local', appName='Orders', conf=conf)
sqlcontext = SQLContext(sc)

folder_path = "C:\\Users\\admin\\Documents\\GitHub\\educate_problems\\pyspark\\input_data"
FILEPATH = os.path.join(folder_path, "orders.csv")

def find_user_last(timestamp, ts_list):
    index_ts = ts_list.index(timestamp)
    if index_ts == 0:
        return 0
    else:
        return int(ts_list[index_ts]) - int(ts_list[index_ts - 1])

def find_last_time():
    my_udf = F.udf(lambda val1, val2: find_user_last(val1, val2), IntegerType())
    df = sqlcontext.read.option("multiline", "true").option("header", "true").csv(FILEPATH)
    df_grouped = df.groupBy("userId").agg(F.collect_list(df.timestamp)) \
        .withColumnRenamed("collect_list(timestamp)", "ts_list")
    df_new = df.join(df_grouped, df['userId'] == df_grouped['userId'], 'left_outer') \
    .drop(df_grouped["userId"])
    df = df_new.withColumn("time_diff", my_udf(df_new["timestamp"], df_new["ts_list"])) \
        .show()

print(find_last_time())

