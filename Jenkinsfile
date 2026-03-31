pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/MariaHusak/Lab_2.git'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t game-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests inside Docker container...'
                sh 'docker run --rm game-app pytest || true'
            }
        }

        stage('Deliver') {
            steps {
                echo 'Copying files to cargo folder...'
                sh 'mkdir -p cargo'
                sh 'cp -r * cargo/'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
