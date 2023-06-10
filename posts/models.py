from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PostModel(models.Model):
    """A model for publishing posts"""

    title = models.CharField('Заголовок', max_length=100)
    comment = models.TextField('Комментарий путешествия')

    coords = models.CharField('Координаты', max_length=64)
    address = models.CharField('Адрес местоположения', max_length=128)

    image_screen_url = models.CharField('Снимок с карты', max_length=1024)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    
