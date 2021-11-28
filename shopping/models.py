from django.db import models

# Create your models here.

class product(models.Model):
    productid=models.AutoField
    produtname=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    category=models.CharField(max_length=30,default="")

    price=models.IntegerField(default="0")
    image=models.ImageField(upload_to="shopping/images",default="")
    publishdate=models.DateField()

# this changes the product name in admin
    def __str__(self):
        return self.produtname


