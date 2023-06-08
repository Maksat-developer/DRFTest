from django.db import models
from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Пользователь должен иметь email!")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password=None):
        
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
        

