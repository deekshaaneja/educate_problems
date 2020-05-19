from pyspark import SparkConf, SparkContext
from pyspark import Broadcast
import os
import sys 

conf = SparkConf().set('spark.driver.host','127.0.0.1')
sc = SparkContext(master='local', appName='myAppName',conf=conf)

folder_path = "C:\\Users\\admin\\Documents\\GitHub\\educate_problems\\pyspark\\input_data"
FILEPATH = os.path.join(folder_path, "testfile.txt")
STOPWORDS_PATH = os.path.join(folder_path, "exclude.txt")

stopwords = set(sc.textFile(STOPWORDS_PATH).collect())
sc.broadcast(stopwords)
input_rdd = sc.textFile(FILEPATH)
words = input_rdd.flatMap(lambda line : line.lower().split())
filtered_words = words.filter(lambda word : word not in stopwords)
word_tuple = filtered_words.map(lambda word: (word, 1))
words_reduced = word_tuple.reduceByKey(lambda value1, value2: value1 + value2)
reverse_pair = words_reduced.map(lambda value : (value[1], value[0]))
sorted = reverse_pair.sortByKey(False)
print(sorted.collect())
for line in sys.stdin:
    print(line)

sc.stop()



