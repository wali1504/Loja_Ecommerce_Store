from django.db import models

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username= models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    password2= models.CharField(max_length=50)
    def __str__(self) -> str:
        
        return f'{self.first_name} , {self.last_name}'
    
class login(models.Model):
     username= models.CharField(max_length=50)
     password = models.CharField(max_length=50)

class AddProduct(models.Model):
      SerialNumber = models.IntegerField(null=True, blank=True)
      ProductName = models.CharField(max_length=50)
      Description = models.CharField(max_length=500)
      Category = models.CharField(max_length=50)
      Price = models.IntegerField()
      StockQuantity = models.IntegerField()

      def __str__(self) -> str:
        
        return f'{self.SerialNumber}-{self.ProductName}'
      
class people(models.Model):
    person_name= models.CharField(max_length=50)
    person_age=models.IntegerField()
    
