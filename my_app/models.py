from django.db import models
from django.contrib.auth.models import User

class TimeTracker(models.Model):
    user = models.ForeignKey(User)
    job = models.CharField(max_length=100)
    # date = models.DateField('%m/%d/%y')
    # time = models.TimeField('%H:%M:%S')
    location = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.job
