# Django specific settings
import inspect  # Importing the inspect module for inspecting live objects
import os  # Importing the os module for operating system related functionalities

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")  # Setting the Django settings module environment variable

from django.db import connection  # Importing the connection module from django.db for database connection

# Ensure settings are read
from django.core.wsgi import get_wsgi_application  # Importing get_wsgi_application function from django.core.wsgi
application = get_wsgi_application()  # Getting the WSGI application object

# Your application specific imports
from orm.models import User  # Importing the User model from orm.models
from datetime import date  # Importing the date class from datetime module

# Delete all data
def clean_data():
    User.objects.all().delete()  # Deleting all data from the User model

# Test Django Model Setup
def test_setup():
    try:
        clean_data()  # Cleaning data before testing
        # Create a test user and save to database
        user = User(first_name='John', last_name='Doe', dob=date(1970, 3, 16))  # Creating a test user object
        user.save()  # Saving the test user object to the database
        # Check user table is not empty
        assert User.objects.count() > 0  # Asserting that the User table is not empty
        print("Django Model setup completed.")  # Printing a success message if setup is completed
    except AssertionError as exception:
        print("Django Model setup failed with error: ")  # Printing an error message if setup fails
        raise(exception)  # Reraising the AssertionError
    except:
        print("Unexpected error")  # Printing an error message for unexpected errors

test_setup()  # Calling the test_setup function to test Django model setup