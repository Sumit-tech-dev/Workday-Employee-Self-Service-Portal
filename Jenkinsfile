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
