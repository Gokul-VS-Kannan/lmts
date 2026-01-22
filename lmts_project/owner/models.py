# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext as _

class Customuser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_mechanic = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_permissions'  # specify custom related name
    )

    # Change the related name for groups
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups'  # specify custom related name for groups
    )

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"
