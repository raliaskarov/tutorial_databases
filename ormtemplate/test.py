"""
This code snippet first cleans the database and then inserts a test object.
Then it checks if the test object was inserted correctly.
"""

# Django specific settings

import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# your application specific imports
from standalone.models import Test

# delete all data
def clean_data():
    Test.objects.all().delete()

# test django model setup
def test_setup():
    try:
        clean_data()
        test = Test(name="name")
        test.save()
        # check test table is not empty
        assert Test.objects.count() > 0
        print("Django Model setup completed.")
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise(exception)
    except:
        print("Unexpected error")

test_setup()
