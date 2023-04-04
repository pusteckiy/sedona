# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN pip install --upgrade pip
# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables for Gunicorn
EXPOSE 8000

# Start Gunicorn to run the Django app
CMD [ "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2" ]