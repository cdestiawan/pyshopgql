from django.db import models

from sorl.thumbnail import ImageField


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    slug = models.SlugField()

    category = models.ForeignKey(
        "category", on_delete=models.SET_NULL, null=True, blank=True, related_name='products')


class Category(models.Model):
    title = models.CharField(max_length=20)


class ProductImage(models.Model):
    image = ImageField(upload_to="products")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images")
