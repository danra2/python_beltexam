from __future__ import unicode_literals
from ..login_regis.models import User
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class TriplanManager(models.Manager):
    def addrip(self, destination,description,user_id,travel_from,travel_to):
        user = User.userManager.get(id=user_id)
        errors = {}
        try:
            users = self.all()
        except:
            users = {}

        if len(destination)<1:
            errors['destination'] = "Destination Field Cannot Be Blank!"

        if len(description)<1:
            errors['description'] = "Description Cannot Be Left Blank!"

        if len(travel_from)<1:
            errors['travel_from'] = "Travel From Date Cannot Be Left Blank!"

        if len(travel_to)<1:
            errors['travel_from'] = "Travel From Date Cannot Be Left Blank!"

        if travel_from > travel_to:
            errors['travel_from'] = "Your Travel To Date Cannot Be After Your From Date! "

        if errors:
            # print errors
            return (False, errors)

        else:
            self.create(destination=destination, description=description, user=user, travel_from=travel_from, travel_to=travel_to)
            return (True, user_id)

class FavlistManager(models.Manager):
    pass

class Triplan(models.Model):
    destination = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    travel_from = models.DateTimeField(auto_now_add = True)
    travel_to = models.DateTimeField(auto_now = True)
    triplanManager = TriplanManager()

class Favlist(models.Model):
    user = models.ForeignKey(User)
    triplan = models.ForeignKey(Triplan)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
