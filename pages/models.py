from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f'{self.full_name} : {self.title}'

