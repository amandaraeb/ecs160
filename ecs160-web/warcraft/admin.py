from django.contrib import admin

# Register your models here.
from warcraft.models import UserProfile

admin.site.register(UserProfile)
