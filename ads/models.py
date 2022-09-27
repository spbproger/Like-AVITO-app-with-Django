from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name