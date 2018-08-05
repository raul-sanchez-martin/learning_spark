package spark.example

/**
  * # Very Simple Spark (Scala) Application to be run on a Spark Cluster
  */

import org.apache.spark.sql.SparkSession

/**
  * @author ${user.name}
  */
object App {

  def main(args : Array[String]) {

    //First we initialize the Spark Session and Spark Context pointing to the Spark Master node
    val spark = SparkSession.builder.appName("Simple Spark App - Cluster").master("spark://localhost:7077").getOrCreate()
    val sc = spark.sparkContext


    //We create an RDD
    val myRDD = sc.parallelize[Int](List(1,2,3))

    // We print the RDD
    println("RDD values: " + myRDD.collect().mkString(", "))
  }

}
