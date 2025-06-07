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
        stage('Deploy') {
            steps {
                bat '%VENV_DIR%\\Scripts\\python.exe manage.py runserver 0.0.0.0:8000'
            }
        }
    }
}