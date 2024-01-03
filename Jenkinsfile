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
	TAG = '0.6'
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

        stage('Build Helm Chart') {
            steps {
                echo 'start build helm chart'
                sh "helm package my-flask-chart"
            }
        }

        stage('Push Helm Chart') {
            steps {
             
                    withCredentials([usernamePassword(credentialsId: 'dockerhublavi', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        helm push my-flask-chart-0.1.5.tgz oci://registry-1.docker.io/lavi324
                        '''
                    }
                
            }
        }
    }

    post {
        success {
            echo 'Docker image and the helm chart pushed successfully.'
        }
    }
}