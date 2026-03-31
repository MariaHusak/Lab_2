pipeline {
    agent any

    environment {
        CARGO_DIR = "D:/cargo"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/MariaHusak/Lab_2.git', branch: 'master'
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat 'python -m pip install --upgrade pip'
                bat 'pip install PySide6 pytest'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                bat 'pytest test.py --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy') {
            steps {
                echo "Copying project to ${CARGO_DIR}"
                bat "xcopy /s /y . ${CARGO_DIR}\\"
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
