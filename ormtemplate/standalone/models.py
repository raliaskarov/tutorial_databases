# models.py
"""
data model 
"""

from django.db import models

# test model
class Test(models.Model):
    name = models.CharField(max_length=30)
