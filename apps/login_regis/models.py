from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
    def login(self, user_name, user_password):
        try:
            user = self.get(user_name = user_name)
        except: return (False, {"Login": "Login Failed"})

        if user and bcrypt.hashpw(user_password.encode('utf-8'), user.user_password.encode('utf-8')) == user.user_password:
            return(True, user)

        else:
            return (False, {"Login": "Login Failed"})

    def register(self, first_name, last_name, user_name, user_password, user_confirm_password):
        errors = {}
        try:
            users = self.all()
        except:
            users = {}

        if len(first_name)<3:
            errors['first_name'] = "First Name is too short"

        if len(last_name)<3:
            errors['last_name'] = "Last Name is too short"

        if len(user_password)<8:
            errors['user_password'] = "Passwords is too short"

        if len(user_name)<3:
            errors['user_password'] = "Passwords is too short"

        if user_password != user_confirm_password:
            errors['user_confirm_password'] = "Passwords must match"

        if errors:
            # print errors
            return (False, errors)

        else:
            password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
            self.create(first_name=first_name, last_name=last_name, user_name=user_name, user_password=password)
            return (True, self.get(user_name=user_name))


    # def input_reivew(self, book_title, author, new_author, user_review, book_rating):

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    user_name = models.CharField(max_length = 50)
    user_password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
