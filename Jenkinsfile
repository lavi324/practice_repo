pipeline {
    agent any

    environment {
        GKE_CLUSTER_NAME = 'lavi-cluster-1'
        GKE_ZONE = 'us-central1'
        KUBE_CONFIG_CREDENTIALS_ID = 'GKE' // Update this line
        DOCKER_HUB_REPO = 'lavi324/practice'
        DOCKER_HUB_IMAGE = 'soccer'
        DOCKER_HUB_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build and push Docker image
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        def customImage = docker.build("${DOCKER_HUB_REPO}/${DOCKER_HUB_IMAGE}:${DOCKER_HUB_TAG}")
                        customImage.push()
                    }
                }
            }
        }

        stage('Update GKE Deployment') {
            steps {
                script {
                    // Configure kubectl with the provided kubeconfig
                    withCredentials([string(credentialsId: "${KUBE_CONFIG_CREDENTIALS_ID}", variable: 'KUBE_CONFIG_FILE')]) {
                        sh "kubectl config set-context --current --kubeconfig=${KUBE_CONFIG_FILE}"
                        
                        // Update the GKE deployment with the new Docker image
                        sh "kubectl set image deployment/flask-app flask-app=${DOCKER_HUB_REPO}/${DOCKER_HUB_IMAGE}:${DOCKER_HUB_TAG} --kubeconfig=${KUBE_CONFIG_FILE}"
                    }
                }
            }
        }
    }
}
