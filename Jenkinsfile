pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "malware-detector"
        DOCKER_TAG = "latest"
        // Replace with your actual Docker Hub username if you want to push
        DOCKER_HUB_USER = "mohamedahsan00" 
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // Build the image using the Dockerfile in the current directory
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Push to Docker Hub') {
             steps {
                script {
                    echo 'Pushing to Docker Hub (Skipping actual push for local assignment)...'
                    // To actually push, you would need credentials configured in Jenkins
                    withCredentials([usernamePassword(credentialsId: 'user', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                        sh "docker login -u $DOCKER_USER -p $DOCKER_PASS"
                        sh "docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_HUB_USER}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                        sh "docker push ${DOCKER_HUB_USER}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                    }
                    echo 'Image successfully pushed to Docker Hub.'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    echo 'Running Container via Docker Compose...'
                    // Ensure the output directory exists on host to avoid permission issues if docker creates it
                    sh "mkdir -p output"
                    sh "mkdir -p network_logs"
                    
                    // Run using docker-compose
                    sh "docker-compose up --abort-on-container-exit"
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh "docker-compose down"
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

