# Specify the base image as Ubuntu
FROM ubuntu

# Install required packages
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pandas numpy seaborn matplotlib scikit-learn scipy

# Create a directory inside the container
RUN mkdir -p /home/doc-bd-a1/

# Move the dataset file to the container
COPY train.csv /home/doc-bd-a1/

# Open the bash shell upon container startup
CMD ["/bin/bash"]
