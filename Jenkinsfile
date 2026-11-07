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
                    python3 -m pip install -r app/requirements.txt
                '''
            }
        }

        stage('Run Application Tests') {
            steps {
                sh '''
                    python3 -m unittest discover -s tests -v
                '''
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }

        failure {
            echo 'CI Pipeline failed. Please check the logs.'
        }
    }
}