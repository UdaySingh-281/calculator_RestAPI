pipeline{
    agent{
        docker{
            image 'python:3.10'
        }
    }

    environment{
        PIP_TARGET = './.venv-packages'
        PYTHONPATH = './.venv-packages'
    }

    stages{

        stage('Install dependencies'){
            steps{
                sh 'pip install --no-cache-dir --target=$PIP_TARGET -r requirements.txt'
            }
        }

        stage('Run Test'){
            steps{
                sh 'PYTHONPATH=$PYTHONPATH python -m pytest --junitxml=report.xml || true'
            }
        }

        stage('Getting the Artifacts'){
            steps{
                junit 'report.xml'
            }
        }
    }

    post{

        success{
            echo '🎉 Build and Tests Successful!'
        }
        unstable{
            echo '⚠️ Tests failed. Build marked as UNSTABLE.'
        }
        failure{
            echo '❌ Build Failed.'
        }
        always{
            echo '✅ Pipeline Finished (Success or Fail).'
        }
    }
}