pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // If using Jenkins "Pipeline script from SCM", this is handled automatically
                echo 'Checking out code...'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv $VENV_DIR'
                sh './$VENV_DIR/Scripts/python -m pip install --upgrade pip'
                sh './$VENV_DIR/Scripts/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh './$VENV_DIR/Scripts/python manage.py test'
            }
        }
    }
}

ALLOWED_HOSTS = ['*']