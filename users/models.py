from django.db import models

from django.contrib.auth.models import (
    AbstractUser
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    profile_photo = models.ImageField('Фото профиля', upload_to='photo/profile/', )
    