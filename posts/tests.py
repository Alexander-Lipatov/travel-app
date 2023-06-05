from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from posts.models import PostModel

User = get_user_model()


class ViewTest(TestCase):
    '''Тест представлений приложения posts'''
    def setUp(self):
        '''Задаем изображение и создаем пользователя 
        с загружаеммым файлом'''

        file = SimpleUploadedFile(
            "test_image.jpg", b"file_content", content_type="image/jpeg")
        self.user = User.objects.create_user(
            username='testuser', password='testpassword', profile_photo=file)
        self.post = PostModel.objects.create(title='Test Post', owner=self.user)

        return super().setUp()

    def test_home_page_status_code_if_not_logged_in(self):
        '''Тест приветственной страницы, когда еще не авторизованны'''

        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, './posts/home.html')
        self.assertEqual(response.status_code, 200)

    def test_home_page_status_code_if_logged_in(self):
        '''Тест отображения домашней страницы 
        в момент когда мы авторизованны'''

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, './posts/posts.html')
        self.assertQuerysetEqual(response.context['posts'], [self.post])
        self.assertEqual(response.status_code, 200)

    def test_create_post_status_code(self):
        '''Тест отображения страницы для создания впечатления'''

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('create-post'))
        self.assertTemplateUsed(response, './posts/create-post.html')
        self.assertEqual(response.status_code, 200)
    
    def test_logout_view(self):
        '''Тест на выход пользователя'''

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertRedirects(response, '/')






