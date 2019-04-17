from __future__ import unicode_literals
from django.db import models

class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title_input']) < 2:
            errors["title_input"] = "Title should be at least 2 characters"
        if len(postData['network_input']) < 3:
            errors["network_input"] = "Network should be at least 3 characters"
        if len(postData['des_input']) < 10:
            errors["des_input"] = "Description should be at least 10 characters"
        return errors

class dbshows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    releasedate = models.DateTimeField()
    descrip = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()
