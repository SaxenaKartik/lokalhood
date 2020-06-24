from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
# Create your models here.

class UserProfileManager(BaseUserManager):

    def create_user(self, phone_no, name, email, password = None):
        if not phone_no:
            raise ValueError("User must have a phone number")

        email = self.normalize_email(email)
        user = self.model(phone_no = phone_no, name = name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_no, name, email, password):
        user = self.create_user(phone_no, name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Model for users in the system"""
    phone_no = PhoneNumberField(unique = True)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = "phone_no"
    REQUIRED_FIELDS = ["email", "name"]

    def get_full_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone_no(self):
        return self.phone_no

    def __str__(self):
        return str(self.name) + " " + str(self.email) + " " + str(self.phone_no)


class Shop(models.Model):
    """ Model for a shop"""
    name = models.CharField(max_length = 100)
    locality = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100, null = True)
    def __str__(self):
        return "name : " + str(self.name) + " locality : " + str(self.locality) + " category : " + str(self.category)

class Request(models.Model):
    """ Model for a request """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE, null = True)
    items = models.CharField(max_length = 500)
    deliver_addr = models.CharField(max_length = 500)
    details = models.CharField(max_length = 500, null = True)
    status = models.IntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "id : " + str(self.id) + " user : " + str(self.user) + " shop : " + str(self.shop) + " items : " + str(self.items) + " deliver_addr : " + str(self.deliver_addr) + " details : "  + str(self.details) + " status : " + str(self.status)
