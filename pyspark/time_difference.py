from pyspark import SparkConf, SparkContext, SQLContext
import pyspark.sql.functions as F
from pyspark.sql.types import ArrayType, IntegerType
from pyspark.sql.window import Window
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
    return int(ts_list[index_ts]) - int(ts_list[index_ts - 1])

def find_last_time():
    my_udf = F.udf(lambda val1, val2: find_user_last(val1, val2), IntegerType())
    df = sqlcontext.read.option("multiline", "true").option("header", "true").csv(FILEPATH)
    df_grouped = df.groupBy("userId").agg(F.sort_array(F.collect_list(df.timestamp))) \
        .withColumnRenamed("sort_array(collect_list(timestamp), true)", "ts_list")
    df_new = df.join(df_grouped, df['userId'] == df_grouped['userId'], 'left_outer') \
    .drop(df_grouped["userId"])
    df = df_new.withColumn("time_diff", my_udf(df_new["timestamp"], df_new["ts_list"])) \
        .show()

def find_last_window():
    my_udf = F.udf(lambda val1, val2: find_user_last(val1, val2), IntegerType())
    df = sqlcontext.read.option("multiline", "true").option("header", "true").csv(FILEPATH)
    df_partitioned = Window.partitionBy("userId").orderBy("timestamp")
    df_new = df.withColumn("ts_list", F.collect_list(df.timestamp).over(df_partitioned))
    df_new.withColumn("time_diff", my_udf(df_new.timestamp, df_new.ts_list)) \
            .show()

def find_time_diff_wind():
    df = sqlcontext.read.option("multiline", "true") \
                .option("header", "true").csv(FILEPATH)
    wind = Window.partitionBy("userId").orderBy(F.col("timestamp"))
    wind_col = F.col("timestamp") - F.lag(F.col("timestamp")).over(wind)
    df_new = df.select("*", wind_col.alias("time_diff")).show()

print(find_time_diff_wind())

