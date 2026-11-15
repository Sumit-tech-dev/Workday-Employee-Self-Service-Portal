pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out application code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    ./venv/bin/python -m pip install --upgrade pip
                    ./venv/bin/pip install -r app/requirements.txt
                '''
            }
        }

        stage('Run Application Tests') {
            steps {
                sh '''
                    ./venv/bin/python -m unittest discover -s tests -v
                '''
            }
        }

        stage('Docker Build') {
            agent {
                label 'docker-agent'
            }
            steps {
                checkout scm
                sh 'docker build -t workday-portal:${BUILD_NUMBER} .'
                sh 'docker images workday-portal'
            }
        }

        stage('Trivy Security Scan') {
            agent {
                label 'docker-agent'
            }
            steps {
                sh '''
                    trivy image \
                    --severity HIGH,CRITICAL \
                    --ignore-unfixed \
                    --exit-code 1 \
                    workday-portal:${BUILD_NUMBER}
                '''
            }
        }

        stage('ECR Push') {
            agent {
                label 'docker-agent'
            }
            steps {
                sh '''
                    set -e

                    AWS_REGION="us-east-1"
                    AWS_ACCOUNT_ID="732088326553"
                    ECR_REPOSITORY="workday-portal"
                    IMAGE_TAG="${BUILD_NUMBER}"

                    ECR_REGISTRY="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

                    aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$ECR_REGISTRY"

                    docker tag "workday-portal:${IMAGE_TAG}" "${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}"

                    docker push "${ECR_REGISTRY}/${ECR_REPOSITORY}:${IMAGE_TAG}"
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }
        failure {
            echo 'CI/CD Pipeline failed. Please check the logs.'
        }
    }
}
