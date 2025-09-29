# admin.py
from django.contrib import admin
from .models import MyInfo,Data

@admin.register(MyInfo)

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')
@admin.register(Data)
class User(admin.ModelAdmin):
    list=('name')