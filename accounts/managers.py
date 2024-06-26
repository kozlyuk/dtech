"""
Custom user model manager for accounts.
"""

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.apps import apps


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, mobile_number, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        model = apps.get_model(app_label='accounts', model_name='User')
        if not email:
            raise ValueError(_('Users must have an email address'))
        if model.objects.filter(email=self.normalize_email(email)).exists():
            raise ValueError(_("User with such email already exist"))
        if not mobile_number:
            raise ValueError(_('Users must have an mobile number'))
        if model.objects.filter(mobile_number=mobile_number).exists():
            raise ValueError(_("User with such mobile number already exist"))
        
        user = self.model(
            email=self.normalize_email(email),
            mobile_number=mobile_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile_number, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(
            email=email,
            mobile_number=mobile_number,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
