Write a web app called Studying Log that allows users to 
log the topics they’re interested in and to make journal entries as 
they study about each topic. The Studying Log home page will 
describe the site and invite users to either register or log in. Once 
logged in, a user can create new topics, add new entries, and read 
and edit existing entries

Create a Virtual Environment
python -m venv sl_env

Activating the Virtual Environment
sl_env\Scripts\activate

Installing Django
pip install django

Creating a Project in Django
django-admin startproject studying_log .

Creating the Database
python manage.py migrate

Viewing the Project
python manage.py runserver
