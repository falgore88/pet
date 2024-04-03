from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.managers import UserManager
from core.models.base import BaseModel

__all__ = ['User']


class User(AbstractBaseUser, BaseModel, PermissionsMixin):
    email = models.EmailField('Email', blank=False, null=False, unique=True)
    is_staff = models.BooleanField(_('Status of staff'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
