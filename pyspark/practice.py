from pyspark import SparkConf, SparkContext, SQLContext
import pyspark.sql.functions as F
from pyspark.sql.types import *
import os
from pyspark.sql.window import Window

conf = SparkConf().set("spark.driver.host", "127.0.0.1").set("spar.sql.shuffle.partitions", "8")
sc = SparkContext(conf=conf, master = "local[*]", appName="Practice")
sqlcontext = SQLContext(sc)

folder_path = "C:\\Users\\admin\\Documents\\GitHub\\educate_problems\\pyspark\\input_data"
FILEPATH = os.path.join(folder_path, "dataset.csv")

def find_rank():
    input_df = sqlcontext.read \
                .option("multiline", "true") \
                .option("header", "true") \
                .csv(FILEPATH)
    wind = Window.partitionBy("depName").orderBy(F.col("salary").desc())
    depNameWind = F.rank().over(wind)
    ranked_df = input_df.select("*", depNameWind.alias("rank")) \
                .where(F.col("rank") <= 2) \
                .show()

def find_avg():
    input_df = sqlcontext.read \
                .option("multiline", "true") \
                .option("header", "true") \
                .csv(FILEPATH)
    wind = Window.partitionBy("depName")
    avg_salary = F.mean(F.col("salary")).over(wind)
    df_with_dep_avg = input_df.select("*", avg_salary.alias("dept_avg")) \
                        .show()

def find_top_n():
    folder_path = os.path.join(os.getcwd(), "pyspark", "input_data")
    PATH = os.path.join(folder_path, 'data_top_n.csv')
    df = sqlcontext.read \
        .option("multiline", "true") \
        .option("header", "true") \
        .csv(PATH)
    wind = Window.partitionBy("category").orderBy(F.col("revenue").desc())
    wind_category = F.dense_rank().over(wind)
    wind_category_rank = F.rank().over(wind)
    wind_category_diff = F.max(F.col("revenue")).over(wind) - F.col("revenue")
    df_ranked = df.select("*", wind_category.alias("dense_rank"), wind_category_diff.alias("diff_from_topmost"), \
                    wind_category_rank.alias("rank")) \
                    .show()

def time_lag():
    folder_path = "C:\\Users\\admin\\Documents\\GitHub\\educate_problems\\pyspark\\input_data"
    FILEPATH = os.path.join(folder_path, "orders.csv")
    df = sqlcontext.read \
        .option("header", "true") \
        .option("multiline", "true") \
        .csv(FILEPATH)
    wind = Window.partitionBy("userId").orderBy("timestamp")
    wind_col = F.col("timestamp") - F.lag(F.col("timestamp")).over(wind)
    df_timelag = df.select("*", F.when(wind_col.isNotNull(), wind_col).otherwise(F.col("timestamp")).alias("lag")) \
                .show()

def running_total():
    folder_path = os.path.join(os.getcwd(), "pyspark", "input_data")
    PATH = os.path.join(folder_path, 'running_total_data.csv')
    df = sqlcontext.read \
            .option("header", "true") \
            .option("multiline", "true") \
            .csv(PATH)
    wind = Window.orderBy("orderQty")
    wind_col = F.sum(F.col("orderQty")).over(wind)
    df_running_total = df.select("*", wind_col.alias("running_total")).show()

def word_count():
    folder_path = "C:\\Users\\admin\\Documents\\GitHub\\educate_problems\\pyspark\\input_data"
    FILEPATH = os.path.join(folder_path, "testfile.txt")
    STOPWORDS_PATH = os.path.join(folder_path, "exclude.txt")
    stopwords = set(sc.textFile(STOPWORDS_PATH).collect())
    sc.broadcast(stopwords)
    input_dataset = sc.textFile(FILEPATH) \
                    .flatMap(lambda line : line.split()) \
                    .filter(lambda word : word not in stopwords) \
                    .map(lambda word : (word, 1)) \
                    .reduceByKey(lambda value1, value2: value1+value2) \
                    .map(lambda tup : (tup[1],tup[0]))  \
                    .sortByKey(False).take(10)
    print(input_dataset)


if __name__ == "__main__":
    # find_rank()
    # find_avg()
    # find_top_n()
    # time_lag()
    # running_total()
    word_count()
