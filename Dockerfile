# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install SSH server and other dependencies
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application into the container
COPY . .

# Expose the port that the app will run on
EXPOSE 8000
EXPOSE 22

# Create SSH key and user for SSH access
RUN useradd -ms /bin/bash myuser && echo 'myuser:mypassword' | chpasswd

# Command to run the application and the SSH server
CMD ["sh", "-c", "service ssh start && uvicorn main:app --host 0.0.0.0 --port 8000"]
