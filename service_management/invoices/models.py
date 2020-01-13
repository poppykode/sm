from django.db import models

from enquiries.models import Enquiry
from accounts.models import User

# Create your models here.

# table for lineitems
class Invoice(models.Model):
    type =models.CharField(max_length=255)
    enquiry = models.ForeignKey(Enquiry,on_delete=models.CASCADE,blank=True,null=True)
    sale_person =  models.ForeignKey(User,on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length = 255)
    banking_details = models.ForeignKey('BankingDetail',on_delete=models.CASCADE,blank=True,null=True)
    total = models.CharField(max_length = 255, default='00,00')
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    company_name = models.CharField(max_length = 255,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    title =  models.CharField(max_length = 255,blank=True,null=True)
    
    def __str__(self): 
        return self.invoice_number

    class Meta:
        ordering = ["-date_created",]


class LineItem(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    title = models.CharField(max_length = 255,blank=True,null=True)
    quantity = models.CharField(max_length = 255,blank=True,null=True)
    description = models.TextField()
    unit_price = models.CharField(max_length = 255,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    line_item_total = models.CharField(max_length = 255)

    def __str__(self): 
        return self.title


class BankingDetail(models.Model):
    company_name =  models.CharField(max_length = 255,unique=True) 
    bank_name = models.CharField(max_length = 255)
    account_number = models.CharField(max_length = 255)
    branch_name = models.CharField(max_length = 255,blank=True, null=True)
    swift_code = models.CharField(max_length = 255,blank=True)
    account_type = models.ForeignKey('AccountType',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.company_name

class AccountType(models.Model):
    account_type = models.CharField(max_length = 255)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.account_type


    
