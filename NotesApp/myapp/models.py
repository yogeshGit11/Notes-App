from datetime import datetime
from email.policy import default
from time import timezone
from django.db import models
from datetime import datetime,date
# Create your models here.
from django.utils import timezone
class mynotes(models.Model):
    topic=models.CharField(max_length=30)
    title=models.CharField(max_length=50)
    note=models.CharField(max_length=200)
    timedate=models.DateTimeField(auto_now=True,null=True)