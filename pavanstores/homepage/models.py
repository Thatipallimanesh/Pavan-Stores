from django.db import models

# Create your models here.

class Foodgrain(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name

class Flour(models.Model): 
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name

class Oil(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(default=100)
    
    def __str__(self):
        return self.name

class Spice(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(default=100)
    
    def __str__(self):
        return self.name

class Dryfruit(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(default=100)
    
    def __str__(self):
        return self.name

class Masala(models.Model):
    product_id = models.AutoField
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(default=100)
    
    def __str__(self):
        return self.name
    

    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    items_json =  models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100,default="")
    def __str__(self):
        return "Order: " + str(self.id)
    
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_description = models.CharField(max_length=5000)
    paymentMethod = models.CharField(max_length=100, default="Cash on Delivery")
    paymentStatus = models.CharField(max_length=100, default="Unpaid")
    delivered = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return "Order: " + str(self.order_id)