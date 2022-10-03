from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MedicalShows(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='')
    type = models.CharField(max_length=100)
    timeadd = models.DateTimeField()

    def __str__(self):
        return self.title
