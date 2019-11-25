from django.db import models
from accounts.models import User
from django.urls import reverse


# Create your models here.
class ProjectInstallationAssessement(models.Model):
    ['Assements', 'Projects', 'Installations']
    STATUS =(
        ('pending','Pending'),
        ('in-progress','In progress'),
        ('on-hold','On hold'),
        ('completed','competed'),
        ('abandoned','Abandoned'),
        )
    TYPE =(
        ('assement','Assement'),
        ('project','Project'),
        ('installation','Installation'),
        )
    type = models.CharField(max_length=255,choices=TYPE)
    title = models.CharField(max_length=255,blank=True, null=True)
    client = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    resources = models.ManyToManyField(User)
    description= models.TextField()
    value = models.CharField(max_length=255,blank=True, null=True)
    status = models.CharField(max_length=255,choices=STATUS,default="pending")

    def  __str__(self): 
        return self.title

    class Meta:
        ordering = ["-timestamp",]

    @property
    def get_html_url(self):
        url = reverse('projects:update_details_pai', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
 
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='comment1_user_set')
    project_installation_assessement = models.ForeignKey(ProjectInstallationAssessement,on_delete=models.CASCADE,blank=True, null=True)
    decription = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def  __str__(self): 
        return str(self.timestamp)

    class Meta:
        ordering = ["-timestamp",]

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    project_installation_assessement = models.ForeignKey(ProjectInstallationAssessement,on_delete=models.CASCADE,blank=True, null=True)
    decription = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    completed = models.BooleanField(default=False)

    def  __str__(self): 
        return self.user.username

    class Meta:
        ordering = ["-timestamp",]
  
    def get_absolute_url(self):
        return reverse('projects:details_pai',self.id)
