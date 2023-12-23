# Use an official Python runtime as a base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory in the container
WORKDIR /BookCatalog

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . .
WORKDIR /BookCatalog

EXPOSE 8000

# Define the command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
