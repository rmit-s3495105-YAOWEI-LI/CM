from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from unittest.util import _MAX_LENGTH

# Create your models here.
class MyUser(models.Model):
    username = User.username
    password=User.password
    permission = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.user.username