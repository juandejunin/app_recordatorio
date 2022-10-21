from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import os
# from apps.cart.models import Cart
# from apps.user_profile.models import UserProfile
# from apps.wishlist.models import WishList

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # sino es email hay un error
        if not email:
            raise ValueError('Users must have an email address')
        # el correo sera igual a la normalizacion de la informacion
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
#CONFIGURAR LA CONTRASEÑA
        user.set_password(password)
#GUARDAR 
        user.save()
        
        return user

# Funcion para crear un super usuario
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    #para saber si un usuario activo la cuenta
    is_active = models.BooleanField(default=True)
    #definir que un usario normal no es miembro de staff
    is_staff = models.BooleanField(default=False)


    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


