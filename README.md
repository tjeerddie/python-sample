# python sample

### setup:
- install python/pip
- install packages with: `pip install -r requirements.txt`
- copy the .env.example file and name it .env
- edit the env to the setting you want to use
- run the migrations: `python manage.py migrate`
- run the seeder: `python manage.py loaddata data`

If you are using mysql as your database:
- create a database with the name from the env file in utf8 format

start the server: `python manage.py runserver`
