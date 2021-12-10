from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# TODO: HELPER (CLASS) FUNCTION: that helps creating the USER or the SUPERUSER.
#  Using the fixture that comes with the BaseUserManager, and overwrites the handler of using email over username.
class UserManager(BaseUserManager):
    # TODO: Creates a user model (self.model(email and all other extra fields)),
    #  and user to set_password of password using BaseUserManager lib,
    #  and lastly save the user (return user). Normalized the email.
    #  If no email, raise ValueError.
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and save a new superuser"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

#######################################################################################################################

# TODO: User Model: Extending from (AbstractBaseUser, PermissionsMixin) for the fixtures.
#  Email field, name field, user is_active set to default True, user is_staff set to default False.
#  Assigning UserManager to the objects attribute.
#  **()-> to be included, as such it creates a new UserManager on the objects.
#  **Setting the USERNAME_FIELD as to using email.
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

#######################################################################################################################
