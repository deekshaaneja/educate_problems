from pyspark import SparkContext, SparkConf, SQLContext
import pyspark.sql.functions as functions
import pyspark.sql.DataFrameStatFunctions as statFunc
from pyspark.sql.types import *
from pyspark.sql.window import Window
import os



filepath = "C:\\Users\\admin\\Documents\\GitHub\\educate_problems\\pyspark\\input_data\\employee\\sample_data.csv"

conf = SparkConf().set("spark.driver.host", "127.0.0.1").set("spark.sql.shuffle.partitions", 8)
sc = SparkContext(conf=conf, master="local[*]", appName="EmployeeApp")
sqlcontext = SQLContext(sc)

def find_avg_total_salary():
    df = sqlcontext.read \
        .option("header", True) \
        .option("multiline", True) \
        .option("quote", "\"") \
        .csv(filepath) 

    windFrame = Window.partitionBy("depName")
    df.select("*", functions.mean(functions.col("salary")).over(windFrame).alias("deptAvg"), \
        functions.sum(functions.col("salary")).over(windFrame).alias("deptSum"),
        functions.collect_list(functions.col("salary")).over(windFrame).alias("salary_list")) \
        .show()

def find_avg_total_salary_ordered():
    df = sqlcontext.read \
        .option("header", True) \
        .option("multiline", True) \
        .option("quote", "\"") \
        .csv(filepath) 

    windFrame = Window.partitionBy("depName").orderBy("salary")
    df.select("*", functions.mean(functions.col("salary")).over(windFrame).alias("deptAvg"), \
        functions.sum(functions.col("salary")).over(windFrame).alias("deptSum"),
        functions.collect_list(functions.col("salary")).over(windFrame).alias("salary_list")) \
        .show()

def find_salary_rank():
    df = sqlcontext.read.option("header", True).option("multiline", True) \
    .option("quote", "\"") \
    .csv(filepath) 

    windFrame = Window.partitionBy("depName").orderBy("salary")
    df.withColumn("rank", functions.rank().over(windFrame)) \
        .withColumn("d_rank", functions.dense_rank().over(windFrame)) \
        .withColumn("row_number", functions.row_number().over(windFrame)) \
        .withColumn("nile", functions.ntile(2).over(windFrame)) \
        .withColumn("per_rank", functions.percent_rank().over(windFrame)) \
        .show()

def frame_boundary():
    df = sqlcontext.read.option("header", True).option("multiline", True) \
    .option("quote", "\"") \
    .csv(filepath) 

    windFrame = Window.partitionBy("depName").orderBy("salary") \
        .rowsBetween(Window.currentRow, 1)
    df.withColumn("salaries", functions.collect_list(functions.col("salary")).over(windFrame)) \
        .show()

def frame_boundary_ordered():
    df = sqlcontext.read.option("header", True).option("multiline", True) \
    .option("quote", "\"") \
    .csv(filepath) 

    windFrame = Window.partitionBy("depName") \
        .rowsBetween(Window.currentRow, 1)
    df.withColumn("salaries", functions.collect_list(functions.col("salary")).over(windFrame)) \
        .show()


if __name__ == "__main__":
    # find_avg_total_salary()
    # find_avg_total_salary_ordered()
    # find_salary_rank()
    # frame_boundary()
    # frame_boundary_ordered()
    find_median()
