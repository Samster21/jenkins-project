pipeline {
    agent { 
        node {
            label 'docker-build-slave'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd app
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                cd app
                python3 main.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
