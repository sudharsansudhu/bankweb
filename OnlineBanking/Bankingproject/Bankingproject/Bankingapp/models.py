from django.db import models

# Create your models here.
class plans(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pic')
    desc = models.TextField()

    def __str__(self):
        return self.name
