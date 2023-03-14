# Why Docker?

## Virtual Environments vs Containers (eg Docker)

Virtual Envs. | Docker
--- | ---
Isolates Python packages | Isolate non-python software
Relies on system level installation of python | Isolates the entire OS and python itself is installed with it

## Steps to build a Dockerized Django project

- Create a new virtual environment and install django
- Create a new Django project within it
- Deactivate virtual environment
- Write a Dockerfile with custom image instructions
- Build the initial image ```docker build .```
- Add a .dockerignore file
- create a docker-compose.yml file
- Spin up the container with ```docker-compose up```
- Always shutdown the container with ```docker-compose down```