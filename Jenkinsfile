pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        IMAGE_NAME = 'weatherdetector:latest'
        CONTAINER_NAME = 'weatherdetector_app'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\python -m pip install --upgrade pip'
                bat '%VENV_DIR%\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat '%VENV_DIR%\\Scripts\\python manage.py test'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }
        stage('Deploy') {
            steps {
                bat 'docker stop %CONTAINER_NAME% || exit 0'
                bat 'docker rm %CONTAINER_NAME% || exit 0'
                bat 'docker run -d --name %CONTAINER_NAME% -p 8000:8000 %IMAGE_NAME%'
            }
        }
    }
}