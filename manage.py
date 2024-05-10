import os  # Importing the os module for operating system related functionalities
import sys  # Importing the sys module for interacting with the Python interpreter

if __name__ == "__main__":  # Checking if the script is being run directly
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")  # Setting the Django settings module environment variable
    try:
        from django.core.management import execute_from_command_line  # Trying to import Django's execute_from_command_line function
    except ImportError:  # Handling ImportError if Django is not found
        try:
            import django  # Trying to import Django if execute_from_command_line is not found
        except ImportError:  # Handling ImportError if Django is not found even after trying to import it
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )  # Raising ImportError with an informative error message
        raise  # Reraising the ImportError if Django import fails
    execute_from_command_line(sys.argv)  # Executing Django management command based on command-line arguments