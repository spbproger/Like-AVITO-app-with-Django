from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

from ads.models import Category, Ad

admin.site.register(Ad)
admin.site.register(Category)

