# Handling Custom User Models in Django

- If migrations have been made at any point before now, deleting all the migration files in the project as well as the postgres volume via Docker desktop is the easiest way to handle the changes.
- Build a new image and spin up the container again.

- It is always important to start  with a Custom User model from the first migrate command else Django will automatically use the default User model and it is dificult to change later on.

- [form.py](https://github.com/3k3n3/pages/blob/main/accounts/forms.py) contains configurations to edit and create custom user.

- [admin.py](https://github.com/3k3n3/pages/blob/main/accounts/admin.py) extends the custom user to the Django admin.

- [tests.py](https://github.com/3k3n3/pages/blob/main/accounts/tests.py) contains tests for userand superuser(admin) creation.

## EXECuting django commands in a Docker container
To execute django commands in the docker container the regular django commands are prefixed with ```docker-compose exec web``` for example running the tests would require you to run ```docker-compose exec web python manage.py test```
In a little more detail:
- docker-compose exec
- web (service that is being invoked)
- python manage.py test (regular django command).