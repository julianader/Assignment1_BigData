#!/bin/bash

# Copy output files from the container to local machine
docker cp container_name:/path/to/output/dpre.csv /path/to/local/bd-a1/service-result/dpre.csv
docker cp container_name:/path/to/output/res_dpre.csv /path/to/local/bd-a1/service-result/res_dpre.csv
docker cp container_name:/path/to/output/eda-in-1.txt /path/to/local/bd-a1/service-result/eda-in-1.txt
docker cp container_name:/path/to/output/eda-in-2.txt /path/to/local/bd-a1/service-result/eda-in-2.txt
docker cp container_name:/path/to/output/eda-in-3.txt /path/to/local/bd-a1/service-result/eda-in-3.txt
docker cp container_name:/path/to/output/vis.png /path/to/local/bd-a1/service-result/vis.png
docker cp container_name:/path/to/output/k.txt /path/to/local/bd-a1/service-result/k.txt

# Stop the container
docker stop container_name
