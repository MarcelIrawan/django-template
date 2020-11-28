from django.db import models
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    """
    override django user model with custom setting
    change username field to email field
    """

    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'users'
    
    def __str__(self):
        return self.email