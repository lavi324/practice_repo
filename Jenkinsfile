pipeline {
    agent any
    environment {
        PROJECT_ID = "My First Project"
        CLUSTER_NAME = "lavi-cluster-1"
        LOCATION = "us-central1"
        CREDENTIALS_ID = 'GKE' 
    }
    stages {
        stage('Scm Checkout') {
            steps {
                git "https://github.com/lavi324/practice_repo/soccertable.py.git"
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t practice_repo/soccertable.py:${env.BUILD_ID} ."
            }
        }
        stage ('push Docker Image') {
            steps {
                withCredentials ([string(credentialsId: 'dockerhub', variable: 'dockerHubCredentials')]) {
                    sh "docker login -u lavi324 -p ${dockerHubCredentials}"
                }
                sh "docker push practice_repo/soccertable.py:${env.BUILD_ID} ."
            }
        }
        stage('Deploy to GKE') {
            steps{
                sh "sed -i 's/tagversion/${env.BUILD_ID}/g' deployment.yaml"
                step([$class: 'KubernetesEngineBuilder',
                    projectId: env.PROJECT_ID, clusterName: env. CLUSTER_NAME,
                    location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env. CREDENTIALS_ID,
		    verifyDeployments: true
                ]}
            }   
        }   
    }   
}   

