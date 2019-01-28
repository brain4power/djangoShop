from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', blank=True, null = True)

    activation_key = models.CharField(max_length=128, verbose_name='код подтверждения', blank=True)
    # срок хранения ключа
    activation_key_expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(48))

    def is_activation_key_expired(self):
        if timezone.now() <= self.activation_key_expires:
            return False
        else:
            return True
