# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .
COPY inference.py .
COPY model.pkl .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create directories for input and output
RUN mkdir -p /input/logs /output

# Run inference.py when the container launches
CMD ["python", "inference.py"]
