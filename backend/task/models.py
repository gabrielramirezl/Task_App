from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=240)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    