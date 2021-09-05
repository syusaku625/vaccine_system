from django.db import models

# Create your models here.
class Hospital(models.Model):
    name=models.CharField(max_length=100)
    prefecture=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    town=models.CharField(max_length=100)

    def __str__(self):
        return '<Hospital:id=' + str(self.id) + ', ' + \
        self.name + ' ' + self.prefecture + ' ' + self.city + ' ' + self.town 