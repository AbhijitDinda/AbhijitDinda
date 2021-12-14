from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'user_type', 'active')


@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ('account', 'title' , 'image', 'category', 'active', 'is_deleted')
