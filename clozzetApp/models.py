from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self, email,password=None, **extra_filds):
        if not email:
            raise ValueError('The Email must be set')
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_filds)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None, **extra_filds):
        extra_filds.setdefault('is_staff',True)
        extra_filds.setdefault('is_superuser',True)
        return self.create_user(self,email,password, **extra_filds)

class User(AbstractBaseUser):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.IntegerField()
    address=models.CharField()
    is_active=models.BooleanField(default=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    objects=UserManager()
                
    def __str__(self):
        return self.name

    


class Category(models.Model):
    
    name = models.CharField(max_length=100)


    def __str__(self):
        return self .name

 

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self .name
