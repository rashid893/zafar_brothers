# Use the official Python image as the base image
FROM python:3

# Set the working directory to /data
WORKDIR /data

# Install Django and Pillow
RUN pip install django Pillow

# Copy the current directory contents into the container at /data
COPY . .

# Run Django migrations


# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
