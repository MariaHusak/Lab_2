pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v /var/jenkins_home/cargo:/cargo'
        }
    }

    environment {
        CARGO_DIR = "/cargo"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/MariaHusak/Lab_2.git', branch: 'master'
            }
        }

    stage('Install dependencies') {
        steps {
            echo 'Creating virtual environment and installing dependencies...'
            sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
            '''
        }
    }

    stage('Run Tests') {
        steps {
            echo 'Running tests with pytest...'
            sh '''
                source venv/bin/activate
                pytest test.py --maxfail=1 --disable-warnings -q
            '''
        }
    }

        stage('Deploy') {
            steps {
                sh 'cp -r * $CARGO_DIR/'
            }
        }
    }

    post {
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed!' }
    }
}
