from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email', max_length=250, unique=True)
    username = models.CharField(max_length=250, verbose_name='Имя', unique=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def __str__(self) -> str:
        return self.username
    
        
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

