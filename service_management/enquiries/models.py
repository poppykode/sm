from django.db import models
import datetime

from accounts.models import User

# Create your models here.

class Enquiry(models.Model):
    STATUS =(('attended','Attended'),('un-attended','Un-Attended'),)
    STATUS_ =(
        ('new','New'),
        ('open','Open'),
        ('lost','Lost'),
        ('won','Won'),
        )
    title = models.CharField(max_length=255,blank=True, null=True)
    priority = models.CharField(max_length=255,blank=True, null=True)
    company = models.CharField(max_length=255,blank=True, null=True)
    contact_name = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(max_length=255,blank=True, null=True)
    phone_number = models.CharField(max_length=255,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    attended_to =models.CharField(max_length=255,choices=STATUS,default="un-attended")
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    priority = models.ForeignKey('Priority',on_delete=models.CASCADE)
    channel = models.ForeignKey('Channel',on_delete=models.CASCADE, related_name='channel')
    service = models.ForeignKey('Service',on_delete=models.CASCADE)
    status = models.CharField(max_length=255,choices=STATUS_,default="new")
    next_follow_up =  models.DateField(blank=True,null=True)
    decription = models.TextField()
    address = models.TextField(blank=True,null=True)
    website = models.URLField(max_length=255,blank=True,null=True)
    service_mode = models.ForeignKey('Channel',on_delete=models.CASCADE, related_name='service_mode',blank=True, null=True)

    def  __str__(self): 
        return self.title

    class Meta:
        ordering = ["-timestamp",]
        verbose_name_plural = "Enquiries"

class Priority(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    colour = models.CharField(max_length=255,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def  __str__(self): 
        return self.title

    class Meta:
        verbose_name_plural = "Priorites"

class Status(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    colour = models.CharField(max_length=255,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def  __str__(self): 
        return self.title

    class Meta:
        verbose_name_plural = "Statuses"

class Channel(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)


    def  __str__(self): 
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)


    def  __str__(self): 
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    enquiry = models.ForeignKey(Enquiry,on_delete=models.CASCADE,blank=True, null=True)
    decription = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def  __str__(self): 
        return str(self.timestamp)

    class Meta:
        ordering = ["-timestamp",]

# class ChangesTracker(models.Model):
#i should be able to track what field was update, enquiry was deleted what user was assignes and by who nd wen





