from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Account, Category, Document, Transaction


@admin.register(Account)
class AccountAdmin(ModelAdmin):
    pass

