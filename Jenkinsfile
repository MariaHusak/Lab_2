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
                echo 'Creating virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install PySide6 pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                    . venv/bin/activate
                    pytest test.py --maxfail=1 --disable-warnings -q
                '''
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
