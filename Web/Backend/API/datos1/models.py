from django.db import models

# Create your models here.
class datos1(models.Model):
    id = models.AutoField(primary_key=True)
    datoT=models.TextField(blank=True)