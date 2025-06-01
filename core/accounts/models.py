from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        
        ('manager', 'Manager'),
        ('student', 'Student')
    )

    email = models.EmailField(verbose_name="ایمیل",unique=True)
    full_name = models.CharField(verbose_name ="نام و نام خانوادگی" , max_length=100)
    user_type = models.CharField(verbose_name="نوع کاربر",max_length=10, choices=USER_TYPES, default='student')
    is_active = models.BooleanField(verbose_name="وضعیت کاربر",default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',  # ← This avoids clash
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',  # ← This avoids clash
        related_query_name='user'
    )

    def __str__(self):
        return self.email
    
    
    class Meta : 
        verbose_name_plural = 'کاربران'