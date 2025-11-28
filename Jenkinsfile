pipeline {
    agent any

    environment {
        DOCKER_USER = "mohamedahsan00"
        IMAGE_NAME = "malware-detector"
        TAG = "latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_USER}/${IMAGE_NAME}:${TAG} ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push ${DOCKER_USER}/${IMAGE_NAME}:${TAG}"
                }
            }
        }

        stage('Prepare Folders') {
            steps {
                sh "mkdir -p network_logs"
                sh "mkdir -p output"
            }
        }

        stage('Run with Docker Compose') {
            steps {
                sh "docker-compose down || true"
                sh "docker-compose up --abort-on-container-exit"
            }
        }
    }

    post {
        always {
            sh "docker-compose down || true"
        }
    }
}
