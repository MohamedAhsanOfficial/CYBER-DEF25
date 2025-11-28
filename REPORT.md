# Lab Assignment 3: AI Malware Detection Container Report

**Name:** [Your Name]  
**Date:** 28-11-25  
**Assignment:** Lab Assignment 3 - CYBER-DEF25 Challenge

---

## 1. Application Overview
The application is an AI-based Malware Detection system packaged as a Docker container. It consists of:
- **inference.py**: The main script that loads a trained model (`model.pkl`), processes logs from `/input/logs`, detects threats, and saves results to `/output/alerts.csv`.
- **model.pkl**: The serialized machine learning model.
- **requirements.txt**: Python dependencies (pandas).

## 2. Docker Configuration
### Dockerfile
The `Dockerfile` packages the application using a Python 3.9 slim image. It installs dependencies and sets up the execution environment.

```dockerfile
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
```

### Docker Compose
The `docker-compose.yml` file defines the service and mounts the host directory `./network_logs` to `/input/logs` in the container, allowing the application to process local log files.

```yaml
version: '3.8'

services:
  malware-detector:
    build: .
    image: malware-detector:latest
    volumes:
      - ./network_logs:/input/logs
      - ./output:/output
    container_name: cyber-def25-inference
```

## 3. Jenkins Pipeline
The `Jenkinsfile` defines a CI/CD pipeline with the following stages:
1. **Build Image**: Builds the Docker image.
2. **Push to Docker Hub**: Pushes the image (simulated for this assignment).
3. **Run Container**: Runs the container using Docker Compose.

```groovy
pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "malware-detector"
        DOCKER_TAG = "latest"
        DOCKER_HUB_USER = "your_dockerhub_username" 
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }
        stage('Push to Docker Hub') {
             steps {
                script {
                    echo 'Pushing to Docker Hub...'
                    // sh "docker push ..."
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    echo 'Running Container via Docker Compose...'
                    sh "mkdir -p output"
                    sh "mkdir -p network_logs"
                    sh "docker-compose up --abort-on-container-exit"
                }
            }
        }
    }
}
```

## 4. Execution Steps & Verification
1. **Setup**: Created `network_logs` directory and added `test_log.txt`.
2. **Build**: Ran `docker-compose build` to create the image.
3. **Run**: Ran `docker-compose up` to start the container.
4. **Output**: The container processed the logs and generated `alerts.csv` in the `output/` directory.

### Sample Output (alerts.csv)
```csv
file,line_number,content,prediction,confidence
test_log.txt,2,2025-11-28 10:00:05 WARN Suspicious activity detected on port 8080,MALWARE_DETECTED,0.98
test_log.txt,4,2025-11-28 10:00:15 ERROR Malware signature found in packet payload,MALWARE_DETECTED,0.98
```

## 5. Conclusion
The application was successfully containerized and orchestrated using Docker Compose. The Jenkins pipeline automates the build and deployment process, meeting all assignment requirements.
