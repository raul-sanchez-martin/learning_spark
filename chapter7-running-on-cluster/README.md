# Running on a Cluster

In this Section, we will briefly explained how to run Spark appliations on a cluster, both in Python and Scala. First, we will explain how to set up a "real" Spark cluster on your computer using Docker. Then, we will discussed how to execute two simple codes (Python and Scala) against the previous cluster:

## Setup a Spark Cluster

In order to setup a Spark cluster as real as possible using a conventional computer, we are going to make use of [Docker](https://www.docker.com/). In particular, we have already set up a docker cluster where we include tree nodes:

* hadoop: The master node of a [Hadoop HDFS](http://hadoop.apache.org/) cluster
* spark-master: The master node of the Spark cluster
* spark-worker-1: The worker node of the Spark cluster

First, you need to install and configure Docker. Please, follow these instructions:

* [Install docker](https://docs.docker.com/install/)
* [Post docker installation](https://docs.docker.com/install/linux/linux-postinstall/)
* [Install docker compose](https://docs.docker.com/compose/install/)

Once all the necessary software has been installed, you can now start your Spark cluster. In order to do that, open a terminal in the `docker-hadoop-spark` folder and type the following command: `docker-compose up`. The cluster will start running. **IMPORTANT: This process can take a long time (several minutes) the first time that is executed as all the Docker images have to be downloaded**

In order to check that everything is working fine, please introduce in your web browser this address: `localhost:8080`. You should see the Spark Web UI.

## Running a Spark Application

Now, we are going to run two applications using the Spark cluster set up in the previous section. Please note that, even that you are going to use the Spark cluster to perform the calculations, you still need to have installed Spark in your computer in order to send that calculation. In this regard, it has to be the same version as the one installed in the cluster. Currently, it is [Spark 2.3.1](https://www.apache.org/dyn/closer.lua/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz)

### Python

A very simple PySpark application is included in the folder `python-project`, in the script `pyspark_app.py`. In this project we just create an RDD and we print it. In order to run the application, please open a terminal in the `python-project` folder and type the following command:

`spark-submit --master spark://localhost:7077 pyspark_app.py`

You should see in the console the printed RDD. Please note that much more information about the process will be printed. In addition, you can open the [Spark Web UI](localhost:8080) and you should see that the application has been executed succesfully.

### Scala

A similar project than the one developed in the previous section can be found in the `scala-project` folder but written in Scala. This project has been built using the [Maven Software Project Management](https://maven.apache.org/) and the IDE [IntelliJ IDEA](https://www.jetbrains.com/help/idea/discover-intellij-idea-for-scala.html), with the Scala plugin.
First, we should compile the project. To to that, open a terminal in the `scala-project` folder and type `mvn clean package`. Once finished, the project will have been compiled in a `.jar` file under the `target` folder. Now, we can run this Spark Application against the cluster. To do that, open a terminal in the `scala-project` folder and type the following command:

`spark-submit --class spark.example.App --master spark://localhost:7077 target/scala-example-1.0-SNAPSHOT.jar`

As for the Python project, you should see in the console the printed RDD. Please note that much more information about the process will be printed. In addition, you can open the [Spark Web UI](localhost:8080) and you should see that the application has been executed succesfully.






