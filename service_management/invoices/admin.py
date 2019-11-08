from django.contrib import admin
from .models import AccountType, BankingDetail,Invoice,LineItem

# Register your models here.
admin.site.register(AccountType)
admin.site.register(BankingDetail)
admin.site.register(Invoice)
admin.site.register(LineItem)
