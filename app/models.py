from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.

class UserManeger(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Fiild is required")
        
        extra_fields['email']=self.normalize_email(extra_fields['email'])
        user= self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        
        return user
    
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    username=models.CharField(max_length=255, unique=True)
    dob = models.DateField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= []

class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    
   
