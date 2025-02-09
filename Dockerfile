# Use an official Python image as the base image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["python", "chatbot.py"]
