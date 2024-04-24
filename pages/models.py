from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=20, verbose_name='تلفن تماس')
    title = models.CharField(max_length=100, verbose_name='موضوع پیام')
    content = models.TextField(verbose_name='متن پیام')

    def __str__(self):
        return f'{self.full_name} : {self.title}'

