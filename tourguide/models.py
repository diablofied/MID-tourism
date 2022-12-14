import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null = True,
    )
    company = models.CharField(max_length=255)
    date = models.DateField(null = True,default=datetime.date.today)
    destination = models.CharField(max_length=255)
    is_booked = models.BooleanField(default=False)
