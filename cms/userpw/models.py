from django.db import models

# Create your models here.
from django.db import models
import hashlib
# Create your models here.
 
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    #last_login = models.DateTimeField(blank=True)
 
    def __unicode__(self):
        return self.username
