from django.db import models

class search(models.Model):
    name = models.TextField(max_length=10)
    city = models.TextField(max_length=10)


    def __str__(self):
        return self.name
