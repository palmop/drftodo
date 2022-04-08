from pyexpat import model
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
    UserManager,
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from datetime import datetime, timedelta
import jwt
from django.conf import settings

from helpers.models import TrackingModel


class UserAppManager(UserManager):
    
    def _create_user(self,  email, username, password, **extra_fields):

        if not username:
            raise ValueError("username mandatory")
        if not email:
            raise ValueError("email mandatory")
        
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username,  password, **extra_fields):

        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, username, password, **extra_fields)


class UserApp(AbstractBaseUser, PermissionsMixin, TrackingModel):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=False, unique=True, )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserAppManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        token = jwt.encode(
            {
                'username': self.username,
                'email': self.email,
                'exp': datetime.utcnow() + timedelta(hours=24),
            },
            settings.SECRET_KEY, 
            algorithm="HS256" 
        )

        return token