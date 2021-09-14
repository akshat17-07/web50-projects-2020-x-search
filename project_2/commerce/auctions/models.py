
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=250)

class Category(models.Model):
    category = models.CharField(max_length=64)

class Listings(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images', max_length=100, null=True, blank=True)
    des = models.CharField(max_length=250)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller_name")
    active = models.BooleanField(default=True)

class Bids(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer_name")
    item = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="item_selling")
    price = models.IntegerField()

class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    item = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="item_sell")
    comment = models.CharField(max_length=250)

class WatchList(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Listings, blank=True)
