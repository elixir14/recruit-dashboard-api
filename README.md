# elixir14-recruit-dashboard-api

After cloning repository move to the Backend dir.
### cd backend

Install require package using below code.
### pip install -r requirments.txt

Fill your database user, password and DB name in local_settings.py

In order to run the migrations initialize Alembic:
### python manage.py db init

Let’s create our first migration by running the migrate command.
### python manage.py db migrate

Now we’ll apply the upgrades to the database using the db upgrade command:
### python manage.py db upgrade

Finally use below command to run the app
### python run.py
