pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-v D:/cargo:/cargo'
        }
    }

    environment {
        CARGO_DIR = "/cargo"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git url: 'https://github.com/yourusername/yourgame.git', branch: 'master'
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip install --upgrade pip'
                sh 'pip install PySide6 pytest'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh 'pytest test.py --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Build / Prepare') {
            steps {
                echo 'Preparing project for deployment...'
                // sh 'pyinstaller --onefile main.py'
            }
        }

        stage('Deploy') {
            steps {
                echo "Copying project to ${CARGO_DIR}"
                sh "cp -r . ${CARGO_DIR}/"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
