#!/bin/bash

docker run -it -p 8888:8888 -p 9999:9999 -v "$PWD":/home/jovyan/work jupyter/all-spark-notebook
