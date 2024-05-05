pipeline {
  agent any

  stages {
      stage("Clone Code") {
          steps {
              echo "Cloning the code"
              git url: "https://github.com/lakshya-chopra/pythonWebApp.git", branch: "main"
          }
      }

      stage("Build") {
          steps {
              echo "Building the Docker image"
              sh "docker build -t myapp ."
          }
      }


      stage("Deploy") {
          steps {
              echo "Deploying the container"
              sh "docker run -it -p 8080:8080 myapp"
              
          }
      }
  }
}
