from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # check email
        email_match = User.objects.filter(email = postData['reg-email'])
        if len(postData['reg-email']) == 0:
            errors['email_blank'] = 'Please enter your email.'
        elif not EMAIL_REGEX.match(postData['reg-email']):
            errors['email_invalid'] = 'Please enter a valid email.'
        elif len(email_match)>0:
            errors['email_invalid'] = 'That email registed already.'
        # check name
        if len(postData['firstname']) == 0:
            errors["firstname-blank"] = "First name cannot leave blank"
        elif len(postData['firstname']) < 2:
            errors["firstname"] = "First name at least 2 characters"
        elif len(postData['lastname']) == 0:
            errors["lastname"] = "Last name cannot leave blank"
        elif len(postData['lastname']) < 2:
            errors["lastname"] = "Last name at least 2 characters"
        elif postData['lastname'].isalpha() == False:
            errors["lastname-alpha"] = "Last name should be only letters"
        # check password
        if len(postData['reg-pw']) == 0:
            errors["pw"] = "Password cannot blank."
        if postData['reg-pw'] != postData['reg-cpw']:
            errors["pw_match_fail"] = "Password not matching, please try again"
        if len(postData['reg-pw']) < 8:
            errors["reg-pw"] = "Password at least 8 characters"
        return errors
    
    def login_validator(self,postData):
        errors = {}
        user = User.objects.filter(email = postData['log-email'])
        if len(postData['log-pw']) == 0:
            errors["pw"] = "Password cannot blank."
        if len(postData['log-email']) == 0:
            errors['email_blank'] = 'Please enter your email.'
        elif not EMAIL_REGEX.match(postData['log-email']):
            errors['email_invalid'] = 'Please enter a valid email.'
        elif not user:
            errors['no-email'] = 'That email does not exits'
        #check password 
        else:
            user = User.objects.get(email = postData['log-email'])
            if bcrypt.checkpw(postData['log-pw'].encode(), user.pword.encode()):
                print('logining in...')
            else:
                errors["pw"] = "Wrong password!"
        return errors

    def update_validator(self, postData):
        errors = {}
        # check email
        email_match = User.objects.filter(email = postData['up-email'])
        if len(postData['up-email']) == 0:
            errors['email_blank'] = 'Please enter your email.'
        elif not EMAIL_REGEX.match(postData['up-email']):
            errors['email_invalid'] = 'Please enter a valid email.'
        elif len(email_match)>1:
            errors['email_invalid'] = 'That email registed already.'
        # check name
        if len(postData['up-fname']) == 0:
            errors["firstname-blank"] = "First name cannot leave blank"
        elif len(postData['up-fname']) < 2:
            errors["firstname"] = "First name at least 2 characters"
        elif len(postData['up-lname']) == 0:
            errors["lastname"] = "Last name cannot leave blank"
        elif len(postData['up-lname']) < 2:
            errors["lastname"] = "Last name  at least 2 characters"
        elif postData['up-lname'].isalpha() == False:
            errors["lastname-alpha"] = "Last name should be only letters"
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()