# Use Ubuntu as the base image
FROM ubuntu

# Update the package lists and install some basic utilities
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Now you can use pip to install packages
RUN pip install python-weather

# Set the working directory in the container
WORKDIR /app

# Copy the weather app from local to WORKDIR
COPY . .

# Adding command to run when running this docker image
CMD ["python3", "python-weather-app.py"]