# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory within the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 9119 for the Flask app to listen on
EXPOSE 9119

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Run the Flask app when the container launches
CMD ["python", "soccertable.py"]
