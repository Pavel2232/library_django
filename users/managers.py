from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):

    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            password=password,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
