from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} has firstname: {self.user.first_name} and email address: {self.user.email}'

class Stock(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name}, {self.description} costs £{self.price}'

class CartItems(models.Model):
    custID = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    stockid = models.ForeignKey(Stock, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)


#=============================================== Creation functions ========================================================

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)