from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
import datetime


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, phone_number, dob,  gender, address, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(
                    email=email, 
                    name=name,
                    phone_number=phone_number,
                    dob=dob,
                    gender=gender,
                    address=address
                )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True)
    dob = models.DateField(default=datetime.date(1990, 1, 1), blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        """Return string representation of our user"""
        return self.email