# Use the official Python 3.8 slim image as the base image
FROM python:3.10-slim

# Get updates
RUN apt-get update -y

# Expose port 80 for the Flask application
EXPOSE 80

# Copy the app files into the container
COPY ./ /app

# Set the working directory and install app requirements
WORKDIR /app
RUN pip install -r requirements.txt

# Set the working directory and run the flask app
WORKDIR /app/web
CMD ["flask", "run", "--host=0.0.0.0", "-p", "80" ]