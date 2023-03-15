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
- Add a .dockerignore file
- Build the initial image ```docker build .```
- Create a docker-compose.yml file
- Spin up the container with ```docker-compose up```
- Always shutdown the container with ```docker-compose down```

## Setting up Postgresql in Docker

- Activate virtual environment
- ```pip install psycopg2``` or ```pip install psycopg2-binary```
- ```pip freeze > requirements.txt``` to update requirements
- Deactivate virtual environment
- Update services in docker-compose.yml with db (database)
- Update settings.py with postgresql configs
- Run ```docker-compose up -d --build``` to build new image and spin up the container - (2-in-1 command)
- Stop container with ```docker-compose down```