from django.db import models
import datetime
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    phone=models.CharField( max_length=10)
    email=models.EmailField( max_length=100)
    password=models.CharField( max_length=100)
    def __str__(self):
        return f'{self.first_name}{self.last_name}'


class Product(models.Model):
    pincode=models.CharField(max_length=250,default='' ,blank=True)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField( max_length=250,default='' ,blank=True)
    image=models.ImageField(upload_to='uploads/product/')
    is_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2,max_digits=6)
    def __str__(self):
        return (self.pincode)
# models.py
class Cart(models.Model):
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return f"Cart  with products {self.product_id}"

 
 

'''class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    

    def __str__(self):
        return f"{self.product.pincode} image"'''

