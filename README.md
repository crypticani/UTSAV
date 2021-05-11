# UTSAV - A sports event management system
## How to use this project
### For Linux
#### Clone this repo
``` 
git clone https://github.com/utsavdsvv/utsav-django.git
```
#### Installing and creating a virtual environment
```
pip install virtualenv
python3 -m venv <env-name>
```
#### Activating virtual environment
```
source <env-name>/bin/activate
```
#### Move to the project's directory
``` 
cd utsav-django
```
#### Install Requirements
```
pip install -r requirements.txt
```
#### Migrate (Apply migrations to create all the database tables)
```
python manage.py migrate
```
#### Create a superuser
```
python manage.py createsuperuser
```
- Starting server
```
python manage.py runserver
```
