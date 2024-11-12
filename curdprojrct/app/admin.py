from django.contrib import admin
from .models import register

# Register your models here.
@admin.register(register)
class registerAdmin(admin.ModelAdmin):
    
    list_display=('id','name','email','password')
    
    
    