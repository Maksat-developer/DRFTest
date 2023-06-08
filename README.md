# INSTALL 
git clone git@github.com:Maksat-developer/DRFTest.git


# Create virtualenv and install requirements.txt
pip3 install -r requiremetns.txt

# Create file .env and write 
SECRET_KEY='django-insecure-b*evh&8dco_m3=1liqd4a9t6xd^5)d830)%e$7fco4127$k)%j'
DATABASE_URL=postgresql://db_name:db_password@localhost:5432/db_username
DJANGO_SETTINGS_MODEL=config.settings
DEBUG=True


# Create migrations
python3 manage.py makemigrations 
python3 manage.py migrate


# Create administration
python3 manage.py createsuperuser


# Run server
python3 manage.py runserver