from typing import Any

from django.shortcuts import redirect

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PostModel
from .forms import PostsForm

from django.views.generic import TemplateView, ListView, CreateView


class HomePageView(ListView):
    '''Данный класс представления отвечает за 
    отображение главной страницы и списка публикаций'''

    template_name = './posts/home.html'
    model = PostModel

    def get_template_names(self):
        '''Данный метод позволит нам сменить шаблон
        в зависимости авторизован user или нет'''
        if self.request.user.is_authenticated:
            self.template_name = './posts/posts.html'  # Шаблон списка публикаций
        return super().get_template_names()

    def get_context_data(self, **kwargs):
        '''пробразываем домолнительные контексты 
        для использования в шаблоне'''
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Получение публикаций только для аутентифицированного пользователя
            posts = PostModel.objects.filter(owner=self.request.user).order_by('-created_date')
            context['posts'] = posts
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    '''Данный класс представления отвечает 
    за отображение формы создания путешествия'''

    model = PostModel
    form_class = PostsForm
    template_name = './posts/create-post.html'
    success_url = '/'
    login_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def logout_view(request):
    '''Данный метод представления отвечает за выход пользователя из системы'''

    logout(request)
    return redirect('home')
