from django.contrib import admin
from hospitalapp.models import contact1

# Register your models here.

class contact_d(admin.ModelAdmin):
    
    list_display = ['cname','cemail','cmobile','cage','cgender','caddress']
    
admin.site.register(contact1,contact_d)
