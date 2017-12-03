from pyspark import SparkContext

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/accessLog.txt", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
pages = pairs.map(lambda pair: (pair[0], pair[1])).distinct().join(pairs.map(lambda pair: (pair[0], pair[1])).distinct()).distinct()
output = pages.map(lambda x: (x[1], x[0])).groupByKey()
output = output.map(lambda x: (x[0], len(x[1]))).filter(lambda x: list(x[0])[0] != list(x[0])[1]).filter(lambda x: x[1] > 2).collect()


for x in output:
    print(x[0], (x[1]))
print ("Popular items done")

sc.stop()