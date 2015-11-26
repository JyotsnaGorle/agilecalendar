from django.contrib.auth.hashers import make_password
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.password = make_password(password=self.password, salt=None, hasher='pbkdf2_sha256')
        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s <%s>" % (self.name, self.email)
