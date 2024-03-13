from django.db import models
from django.shortcuts import reverse
from django_jalali.db import models as jmodels
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product/product_images')
    active = models.BooleanField(default=True)
    datetime_created = jmodels.jDateTimeField(auto_now_add=True)
    datetime_modified = jmodels.jDateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.pk])


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name + ':' + self.product.title

