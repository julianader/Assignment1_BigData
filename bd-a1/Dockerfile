FROM ubuntu:20.04

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    && pip3 install --upgrade pip \
    && pip3 install pandas numpy seaborn matplotlib scikit-learn scipy \
    && apt-get install -y docker.io

# Create directory for the dataset
RUN mkdir -p /home/doc-bd-a1/

# Copy the dataset into the container
COPY train.csv /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Specify the command to run when the container starts
CMD ["python3", "load.py", "/home/doc-bd-a1/train.csv"]
