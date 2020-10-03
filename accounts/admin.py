from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_no','permission')
    model = Profile
    con_delete = False

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)