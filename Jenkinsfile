pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'lavi324/practice_repo'
        IMAGE_NAME = 'soccertable'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git 'https://github.com/lavi324/practice_repo.git'
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_REPO}/${IMAGE_NAME}", '-f Dockerfile .')
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        docker.image("${DOCKER_HUB_REPO}/${IMAGE_NAME}").push()
                    }
                }
            }
        }
    }
}
