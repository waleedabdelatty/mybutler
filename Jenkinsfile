pipeline{
  agent any
  parameters{
    booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests during the build')
  }
  stages{
    stage('Clone'){
      steps {
        echo "Starting Cloning ....."
        git clone "https://github.com/waleedabdelatty/mybutler.git"
        echo "repo cloned successfully"
      }
    }
    stage ('Testing') {
      steps{
        echo "this wont run"
        script{
          if (params.RUN_TESTS){
            echo "why am ÷ running"
          } else {
            // this is a comment 
            echo " Skipping Testing ..."
          }
          }
        }
      }
    stage('Build Docker'){
      steps{
        echo 'Building the Docker image...'
        script{
          docker.build("appy:${env.BUILD_NUMBER}")
        }
      }
    }
    stage('Well done'){
      steps{
        echo "Bravo Bravo"
        echo "Pipeline succeeded"

      }
    }
  }
}
