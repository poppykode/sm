from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User (AbstractUser):
    DES =(
        ('admin','Admin'),
        ('sales','Sales'),
        ('tech','Technician'),
        ('cs','Customer Services'),)
    is_sales = models.BooleanField(default=False)
    is_technician = models.BooleanField(default=False)
    is_customer_services = models.BooleanField(default=False)
    designation = models.CharField(max_length=30,choices=DES,default='admin')
    

    def __str__(self): 
        return self.username

    class Meta:
        ordering = ["-date_joined",]


class ProfilePicture(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): 
            return str(self.date_created)