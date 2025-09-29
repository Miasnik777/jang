# admin.py
from django.contrib import admin
from .models import MyInfo,Data

@admin.register(MyInfo)
@admin.register(Data)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')
class User(admin.ModelAdmin):
    list_display=('name')