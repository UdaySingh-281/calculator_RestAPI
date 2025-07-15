pipeline{
    agent{
        docker{
            image 'python:3.10'
        }
    }

    environment{
        PIP_TARGET = './.venv-packages'
        PYTHONPATH = '/.venv-packages'
    }

    stages{

        stage('Install dependencies'){
            steps{
                sh 'pip install --no-cache-dir --target=$PIP_TARGET -r requirements.txt'
            }
        }

        stage('Run Test'){
            steps{
                sh 'python -m unitest discover .'
            }
        }
    }
}