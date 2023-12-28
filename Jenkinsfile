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

        stage('Build Docker Image') {
            steps {
		echo 'start build docker image'
            	sh "docker build -t latest ."   
            }
        }

        stage('Push Docker Image') {
            steps {
             
                    withCredentials([usernamePassword(credentialsId: 'dockerhublavi', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push lavi324/practice:latest
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

