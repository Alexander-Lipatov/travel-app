import requests

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def save_profile_photo(backend, user, response, *args, **kwargs):
    if not default_storage.exists(user.profile_photo.name):
        if backend.name == 'vk-oauth2':
            # Подстройте название поля в соответствии с ответом провайдера
            photo_url = response.get('photo')
            if photo_url:
                # Скачиваем фото и сохраняем его в поле profile_photo пользователя
                user.profile_photo.save(f'{user.username}_profile_photo.jpg', ContentFile(
                    requests.get(photo_url).content), save=True)
