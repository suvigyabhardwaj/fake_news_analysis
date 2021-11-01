from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class History(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    news=models.CharField(max_length=2000)
    prediction=models.CharField(max_length=10)

    def __str__(self):
        return self.news