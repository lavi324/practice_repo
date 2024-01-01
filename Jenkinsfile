pipeline {
    agent {
        kubernetes {
            inheritFrom 'docker-image-build'
            idleMinutes 5
            yamlFile 'Build-pod.yaml'
            defaultContainer 'dind'
        }
    }

    environment {
        DOCKER_REGISTRY = 'https://registry.hub.docker.com'
        DOCKER_HUB_CREDENTIALS = credentials('dockerhublavi') 
    }

    stages {
        stage('Test Docker') {
            steps {
                script {
                    sh 'docker --version'
                }
            }
        }

        stage('Determine Next Tag') {
            steps {
                script {
                    def currentTag = sh(script: 'curl -s "https://registry.hub.docker.com/v2/repositories/lavi324/practice/tags/" | jq -r ".results[].name" | sort -V | tail -n 1', returnStdout: true).trim()
                    def nextTag = currentTag.toBigDecimal() + 0.1

                    // Set the next tag as an environment variable for later stages
                    env.TAG = nextTag.toString()
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Start build docker image'
                sh "docker build -t lavi324/practice:${TAG} ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhublavi', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push lavi324/practice:${TAG}
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image pushed successfully.'
        }
    }
}
