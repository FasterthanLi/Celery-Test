from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import uuid
from main.tasks import send_verification_email
from django.db.models import signals

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    phone_number = models.CharField(verbose_name='phone number', max_length=20, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=False)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=False)
    is_verified = models.BooleanField(verbose_name = 'verified', default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    verification_uuid = models.UUIDField(verbose_name ='Unique Verification UUID', default=uuid.uuid4)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email 
         send_verification_email.delay(instance.pk)

signals.post_save.connect(user_post_save, sender=User)