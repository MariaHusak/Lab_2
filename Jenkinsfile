pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/MariaHusak/Lab_2.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t game-app .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run game-app pytest'
            }
        }

        stage('Deliver') {
            steps {
                sh 'mkdir -p cargo'
                sh 'cp -r * cargo/'
            }
        }
    }
}
