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
