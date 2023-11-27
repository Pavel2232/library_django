from django.contrib.auth.base_user import AbstractBaseUser

from users.managers import UserManager
from django.db import models


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(max_length=255, null=False,unique=True, verbose_name='Почта')
    is_active = models.BooleanField(default=True)
    data_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name']

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email