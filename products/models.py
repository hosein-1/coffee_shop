from django.db import models
from ckeditor.fields import RichTextField
from django_jalali.db import models as jmodels


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
