from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['firstname']) < 2:
            errors["firstname"] = "First name should be at least 5 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "Last name should be at least 2 characters"
        if postData['pw'] != postData['cpw']:
            errors["pw"] = "Password not matching, please try again"
        if len(postData['pw']) < 8:
            errors["pw"] = "Password should be at least 8 characters"
        return errors

class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    pword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messuser")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="cmmess")
    user = models.ForeignKey(User, related_name="cmuser")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
