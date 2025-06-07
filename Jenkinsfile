pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv %VENV_DIR%'
                sh '%VENV_DIR%\\Scripts\\python -m pip install --upgrade pip'
                sh '%VENV_DIR%\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '%VENV_DIR%\\Scripts\\python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                // This will start the Django server on localhost:8000 in a new window
                bat 'start "" "%CD%\\%VENV_DIR%\\Scripts\\python.exe" manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}