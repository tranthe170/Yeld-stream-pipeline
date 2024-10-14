# Extend the spark-base image
FROM spark-base

# Arguments for versions
ARG SPARK_VERSION=3.4.0
ARG JUPYTERLAB_VERSION=3.1.10


# Install Jupyter and PySpark
RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install wget pyspark==${SPARK_VERSION} jupyterlab==${JUPYTERLAB_VERSION}

# Create the /opt/notebooks directory
RUN mkdir -p /opt/notebooks

# Expose Jupyter notebook port
EXPOSE 8888

# Set working directory to /opt/notebooks
WORKDIR /opt/notebooks

# Start Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
