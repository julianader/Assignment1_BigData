#!/bin/bash

# Copy output files from the container to local machine
docker cp Assignment_1:C:/Users/pc/Desktop/Assignment1_BigData/bd-a1/service-result/dpre.csv
docker cp Assignment_1:C:/Users/pc/Desktop/Assignment1_BigData/bd-a1/service-result/res_dpre.csv
docker cp Assignment_1:C:/Users/pc/Desktop/Assignment1_BigData/bd-a1/service-result/eda-in-1.txt
docker cp Assignment_1:C:/Users/pc/Desktop/Assignment1_BigData/bd-a1/service-result/eda-in-2.txt
docker cp Assignment_1:C:/Users/pc/Desktop/Assignment1_BigData/bd-a1/service-result/eda-in-3.txt
docker cp Assignment_1:C:/Users/pc/Desktop/Assignment1_BigData/bd-a1/service-result/vis.png
docker cp Assignment_1:C:/Users/pc/Desktop/Assignment1_BigData/bd-a1/service-result/k.txt

# Stop the container
docker stop Assignment_1
