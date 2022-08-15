from django.contrib import admin
from .models import Company
#registering model to admin site
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['companyName','emailId', 'companyCode', 'Strength', 'website','created_time']
