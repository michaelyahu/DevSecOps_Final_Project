pipeline {
    agent any
    
    stages {
        stage('Clean Up') {
            steps {
                // Clean up existing containers and images
                script {
                    sh 'docker stop $(docker ps -a -q) || true'
                    sh 'docker rm $(docker ps -a -q) || true'
                    sh 'docker rmi $(docker images -q) || true'     
                }
            }
        }

        stage('Git Clone') {
            steps {
                // 2. Git clone repo 
                script {
                    sh 'git clone git@github.com:michaelyahu/personal-projects.git/DevSecOps_Final_Project.git'
                }
                script{
                sleep(time:10,unit:"SECONDS")
                }
            }
        }

        stage('Docker Build') {
            steps {
                // 3. Docker build
                script {
                    sh 'DOCKER_BUILDKIT=0 docker build . -t endprojent:one'
                }
                script{
                sleep(time:10,unit:"SECONDS")
                }
            }
        }

        stage('Docker Run') {
            steps {
                // 4. Docker run for the new image
                script {
                    sh 'docker run -d --name test_end_project -p 8000:8000 endprojent:one '
                }
                script{
                sleep(time:10,unit:"SECONDS")
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Cleanup Docker images and containers
                script {
                    sh 'docker stop end_projent_test || true'
                    sh 'docker rm end_projent_test || true'
                    sh 'docker rmi end_projent || true'
                    sh 'cd /var/jenkins_home/workspace/'
                    sh 'rm -rf *'
                }
            }
        }
    }
}