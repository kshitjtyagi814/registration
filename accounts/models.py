from django.db import models

# Create your models here.
class account(models.Model):
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    email= models.EmailField()
    address1= models.CharField(max_length=100)
    address2= models.CharField(max_length=200)
    address3= models.CharField(max_length=200)
    mobilenumber= models.CharField(max_length=15)
    country= models.CharField(max_length=200)
    state= models.CharField(max_length=200)
    zip= models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

    def mob(self):
        return self.mobilenumber


    class Meta:
        db_table:"accounts_account"
