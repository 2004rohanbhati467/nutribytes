from django.db import models

class Registered_users(models.Model):
    Username=models.TextField(max_length=50)
    password=models.CharField(null=False,blank=False)