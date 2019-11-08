from django.db import models

from accounts.models import User
from enquiries.models import Service,Priority


# Create your models here.


class FaultyLogging(models.Model):
    STATUS = (
        ('open', 'Open'),
        ('wip', 'Work In Progress'),
        ('closed', 'Closed'),
    )

    title = models.CharField(max_length=255, blank=True, null=True)
    priority = models.ForeignKey(Priority,on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    assigned_to = models.ManyToManyField(
        User, blank=True)
    status = models.CharField(max_length=255, choices=STATUS, default="open")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    faulty_decription = models.TextField()
    faulty_close_date = models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='comment_user_set')
    fault = models.ForeignKey(FaultyLogging,on_delete=models.CASCADE,blank=True, null=True)
    decription = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def  __str__(self): 
        return str(self.timestamp)
