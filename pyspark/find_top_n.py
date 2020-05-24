from pyspark import SparkConf, SparkContext, SQLContext
import pyspark.sql.functions as F
import os
from pyspark.sql.window import Window

folder_path = os.path.join(os.getcwd(), "pyspark", "input_data")
PATH = os.path.join(folder_path, 'data_top_n.csv')

conf = SparkConf().set("spark.driver.host", "127.0.0.1").set("spark.sql.crossJoin.enabled", "true") \
        .set("spark.sql.shuffle.partitions", "8")
sc = SparkContext(master='local', appName='Rank', conf=conf)
sqlsc = SQLContext(sc)

def find_top_n():
    input_df = sqlsc.read \
                .option("multiline", "true") \
                .option("header", "true") \
                .csv(PATH)
                # .show()

    wind = Window.partitionBy("category").orderBy(F.col("revenue").desc())
    ranked_col = F.rank().over(wind)
    ranked_df = input_df.select("*", ranked_col.alias("ranked")) \
                    .where(F.col("ranked") <= 2) \
                        .show()

def revenue_diff_per_category():
    input_df = sqlsc.read \
                .option("multiline", "true") \
                .option("header", "true") \
                .csv(PATH)
    wind = Window.partitionBy("category").orderBy(F.col("revenue").desc())
    revenue_diff = F.max(F.col("revenue")).over(wind) - F.col("revenue")
    revenue_diff_df = input_df.select("*", revenue_diff.alias("diff")) \
                        .show()

if __name__ == "__main__":
    # print(find_top_n())
    print(revenue_diff_per_category())
