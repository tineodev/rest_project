from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.URLField(max_length=255)

    class Meta:
        db_table = 'Api-Services'