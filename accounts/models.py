from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager



class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name='ایمیل',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(max_length=60, blank=True, null=True, verbose_name=('نام کامل'))
    profile_user = models.ImageField(upload_to='profile_user', null=True, blank=True, verbose_name='عکس پروفایل')
    is_author = models.BooleanField(default=False, verbose_name='کاربر نویسنده')
    is_active = models.BooleanField(default=True, verbose_name='کاربر فعال')
    is_admin = models.BooleanField(default=False, verbose_name='کاربر ادمین')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):

        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):

        return self.is_admin
