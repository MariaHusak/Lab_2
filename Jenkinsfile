pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/MariaHusak/Lab_2.git'
            }
        }

        stage('Build & Test') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u'
                }
            }
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt || true'
                sh 'pytest || true'
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
