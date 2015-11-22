import hashlib

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True, primary_key=True)

    def save(self, *args, **kwargs):
        self.password = hashlib.sha512(self.password).hexdigest()
        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
