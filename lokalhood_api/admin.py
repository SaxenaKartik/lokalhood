from django.contrib import admin
from lokalhood_api import models
# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Shop)
admin.site.register(models.Request)
