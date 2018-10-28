## Spark Application - execute with spark-submit

## Imports
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

## Module Constants
APP_NAME = "Spark-Streaming"
my_spark = None

## Closure Functions
def manage_line(line):
    first_split = line.replace('{', '').replace('}', '').split(',')
    name = first_split[0].strip().split(':')[1][2:-1]
    time = first_split[1].strip().split(':')[1][2:-1]
    pri = first_split[3].strip().split(':')[1][2:-1]
    ttlqty = first_split[4].strip().split(':')[1][2:-1]
    ttlmon = first_split[5].strip().split(':')[1][2:-1]

    result = (name, time, pri, ttlqty, ttlmon)
    return result

def manage_info(tup):
    return ((tup[0], tup[1]), (eval(tup[2]), eval(tup[3]), eval(tup[4])))

def reduce(x, y):
    return (x[0] , x[1]+y[1],x[2]+y[2])

def restore(t):
    return (t[0][0],t[0][1],t[1][0],t[1][1],t[1][2])

def avg_price(t):
    return (t[0],t[1],float(t[4]/t[3]),t[3],t[4])


def insertMongo(rdd):
    if not rdd.isEmpty():
        print(rdd.collect())
        my_spark.createDataFrame(rdd.collect(), ["Stknme", "Trdtim", "Avgpri", "Ttlqty", "Ttlmon"]).write.format("com.mongodb.spark.sql.DefaultSource").mode("append").save()

## Main functionality

def main(sc):
    ssc = StreamingContext(sc, 15)
    # lines = ssc.textFileStream('C:\\usr\\Code\\python_code\\sim_sparkstreaming\\test-data')
    lines = ssc.textFileStream('file:///root/sim_dataset/')
    #
    element = lines.flatMap(lambda a: a.split('\n'))
    dayinfo = element.map(manage_line).map(manage_info)
    result = dayinfo.reduceByKey(reduce).map(restore).map(avg_price)
    result.pprint()


    global my_spark
    my_spark = SparkSession \
        .builder \
        .appName("test db") \
        .config("spark.mongodb.output.uri", "mongodb://188.xxx.xxx.xxx/stock.transaction_result") \
        .getOrCreate()

    result.foreachRDD(insertMongo)



    # people = my_spark.createDataFrame(
    #     [("Bilbo Baggins", 50), ("Gandalf", 1000), ("Thorin", 195), ("Balin", 178), ("Kili", 77),
    #      ("Dwalin", 169), ("Oin", 167), ("Gloin", 158), ("Fili", 82), ("Bombur", None)], ["name", "age"])
    # people.write.format("com.mongodb.spark.sql.DefaultSource").mode("append").save()

    ssc.start()
    ssc.awaitTermination()


if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setAppName(APP_NAME)
    # conf = conf.setMaster("local[*]")
    conf = conf.setMaster("spark://192.168.0.2:7077")
    sc = SparkContext(conf=conf)


    # Execute Main functionality
    main(sc)
