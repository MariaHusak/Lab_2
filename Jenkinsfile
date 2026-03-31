pipeline {
    agent any

    environment {
        CARGO_DIR = "/var/jenkins_home/cargo"
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
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install PySide6 pytest'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh 'pytest test.py --maxfail=1 --disable-warnings -q'
            }
        }

        stage('Deploy') {
            steps {
                echo "Copying project to ${CARGO_DIR}"
                sh 'mkdir -p $CARGO_DIR'
                sh 'cp -r * $CARGO_DIR/'
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
