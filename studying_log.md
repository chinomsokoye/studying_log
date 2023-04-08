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


python manage.py makemigrations studying_logs

python manage.py migrate

Creating a Superuser
python manage.py createsuperuser

username - chinom
email - chinomsokoye@aol.com
password - Chioarhe@1

Django Shell
python manage.py shell

from studying_logs.models import Topic, Entry
topics = Topic.objects.all()
entries = Entry.objects.all()
for topic, entry in topics, entries:
    print(topic.id, entry.id, topic, entry)

t = Topic.objects.all()
t.text
t.date_added

