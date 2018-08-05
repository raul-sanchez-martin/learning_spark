# Very Simple PySpark Application to be run on a Spark Cluster

from pyspark.sql import SparkSession

if __name__ == "__main__":

    # First we initialize the Spark Session and Spark Context pointing to the Spark Master node
    spark = SparkSession.builder.appName("Simple PySpark App - Cluster").master("spark://localhost:7077").getOrCreate()
    sc = spark.sparkContext

    # We create an RDD
    rdd = sc.parallelize([1,2,3,4])

    # We print the RDD
    print("RDD values: {0}".format(rdd.collect()))