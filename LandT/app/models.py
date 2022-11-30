from django.db import models

class products(models.Model):
    product_name = models.CharField(max_length=50)
    prise = models.IntegerField()
    image = models.ImageField(upload_to='products_img')