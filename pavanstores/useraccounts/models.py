from django.db import models

# Create your models here.

class User_cart(models.Model):
    user_email = models.CharField(max_length=100, default="")
    items_json = models.CharField(max_length=10000, default="")
    def __str__(self):
        return "cart: " + str(self.user_email)