# Dockers examples 
The code provided is a collection of examples and configurations for running Python applications in Docker containers.

The `single_app_example` directory contains an example of a FastAPI application that uses multiprocessing to generate and consume data.The tmp.py file defines the FastAPI routes and starts the application.The camera.py file defines a Camera class that uses multiprocessing to generate data and insert it into a queue.The generated data is then consumed and processed by another process.

The `Jupyterlab_Dockerfile_devContainer` directory contains a Dockerfile and devcontainer configuration for running JupyterLab in a Docker container and working with it in the VS Code dev container.

The `pyspark_docker-compose_devContainer` directory contains a Docker Compose configuration for running a PySpark application in a Docker container and working with it in the VS Code dev container.

Each directory contains a readme.md file that provides instructions and explanations for running the examples and configurations.

Overall, this repository provides examples and configurations for running Python applications in Docker containers and working with JupyterLab, and PySpark.