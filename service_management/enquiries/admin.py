from django.contrib import admin
from .models import (
    Enquiry,
    Priority,
    Status,
    Service,
    Channel,
    Comment,
)

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Service)
admin.site.register(Channel)
admin.site.register(Comment)

