# admin.py
from django.contrib import admin
from .models import MyInfo

@admin.register(MyInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')