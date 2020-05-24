from pyspark import SparkConf, SparkContext, SQLContext
import pyspark.sql.functions as F
from pyspark.sql.types import ArrayType, IntegerType
import os
import sys
from pyspark.sql.window import Window


conf = SparkConf().set("spark.driver.host", "127.0.0.1").set("spark.sql.crossJoin.enabled", "true") \
        .set("spark.sql.shuffle.partitions", "8")
sc = SparkContext(master='local', appName='Rank', conf=conf)
sqlsc = SQLContext(sc)

folder_path = "C:\\Users\\admin\\Documents\\GitHub\\educate_problems\\pyspark\\input_data"
FILEPATH = os.path.join(folder_path, "dataset.csv")

def find_rank():
    df = sqlsc.read \
        .option("header", True) \
        .csv(FILEPATH)
    by_dept_name_salary_desc = Window.partitionBy("depName").orderBy(F.col("salary").desc())
    rank_by_dept_name = F.rank().over(by_dept_name_salary_desc)
    df_rank = df.select("*", rank_by_dept_name.alias("rank"))
    df_rank.where(df_rank.rank <= 2).show()
    print("1")

find_rank()