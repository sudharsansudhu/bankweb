from django.db import models

# Create your models here.
class fill(models.Model):
    username=models.CharField(max_length=250,null=True)
    password=models.IntegerField(null=True)

    def __str__(self):
        return self.username
