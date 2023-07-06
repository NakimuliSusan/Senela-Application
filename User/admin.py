from django.contrib import admin
from .models import User


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'userName', 'email','phoneNumber') 
    search_fields = ('firstName', 'userName')
admin.site.register(User, UserAdmin)

