from django.db import models

from django.contrib.auth.models import User

from decimal import Decimal

from django.urls import reverse


class PageView(models.Model):
    hostname = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=True) # set to False so it required user must fill in
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    #upload an image
    picture = models.ImageField(upload_to='item_images/')
    class Meta:
        ordering = ['date_end']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('welcome:itemDetail', kwargs={'pk':self.pk})
class Bid(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=6, default=Decimal(0))
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    def __str__(self):
        return str(self.user.username) + " bids " +  str(self.price) + " on " + str(self.item.title)
    def get_absolute_url(self):
        return reverse('welcome:itemDetail', kwargs={'pk':self.item.pk})
